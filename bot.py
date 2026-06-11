"""
bot.py — Solo Leveling Discord Bot
====================================
• Auto-loads every cog file inside the /cogs folder
• Case-insensitive prefix  sl  (sl, Sl, SL, sL, etc.)
• Default help command removed — replaced by advanced category help (HelpCog)
• DB status command (admin-only) pings both SQLite and MongoDB
"""

import os
import json
import logging
import asyncio
from pathlib import Path

import discord
from discord.ext import commands

from database import init_databases, close_databases, MongoDB, sqlite_conn

# ─────────────────────────────────────────────────────────────
# Logging
# ─────────────────────────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-8s  %(name)s — %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger("bot")

# ─────────────────────────────────────────────────────────────
# Config
# ─────────────────────────────────────────────────────────────
CONFIG_PATH = Path("config.json")

def load_config() -> dict:
    with open(CONFIG_PATH, "r") as f:
        return json.load(f)

# ─────────────────────────────────────────────────────────────
# Case-insensitive prefix  →  sl / Sl / SL / sL
# ─────────────────────────────────────────────────────────────
def get_prefix(bot: commands.Bot, message: discord.Message):
    return ["sl ", "Sl ", "SL ", "sL ", "sl", "Sl", "SL", "sL"]  # fallback (discord.py needs at least one returned value)

# ─────────────────────────────────────────────────────────────
# Bot instance  (no default help)
# ─────────────────────────────────────────────────────────────
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(
    command_prefix=get_prefix,
    intents=intents,
    help_command=None,        # ← removed; HelpCog handles this
    case_insensitive=True,
)

# ─────────────────────────────────────────────────────────────
# Auto-load every *.py file inside the cogs/ folder
# ─────────────────────────────────────────────────────────────
async def load_all_cogs() -> None:
    """Load cogs in the correct dependency order defined in cogs/EXTENSIONS.py."""
    from cogs.EXTENSIONS import ALL_EXTENSIONS

    for module in ALL_EXTENSIONS:
        try:
            await bot.load_extension(module)
            log.info("  ✔  Loaded cog: %s", module)
        except Exception as exc:
            log.error("  ✘  Failed to load %s: %s", module, exc)

# ─────────────────────────────────────────────────────────────
# Bot events
# ─────────────────────────────────────────────────────────────
@bot.event
async def on_ready():
    log.info("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    log.info("🗡️  %s  is online  (ID: %s)", bot.user, bot.user.id)
    log.info("   Guilds : %d  |  Cogs: %d", len(bot.guilds), len(bot.cogs))
    log.info("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    await bot.change_presence(
        status=discord.Status.idle,
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name="Arise | slhelp",
        )
    )

@bot.event
async def on_command_error(ctx: commands.Context, error):
    if isinstance(error, commands.CommandNotFound):
        return   # silently ignore unknown commands
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"⚠️ Missing argument: `{error.param.name}`. Use `slhelp` for usage.")
        return
    if isinstance(error, commands.CheckFailure):
        await ctx.send("🚫 You don't have permission to use that command.")
        return
    log.exception("Unhandled command error in %s:", ctx.command, exc_info=error)

# ─────────────────────────────────────────────────────────────
# Entry point
# ─────────────────────────────────────────────────────────────
async def main():
    config = load_config()
    token  = config.get("token") or os.getenv("DISCORD_TOKEN")
    if not token:
        raise RuntimeError("No Discord token found in config.json or env DISCORD_TOKEN.")

    # Init both databases in a thread pool (blocking calls)
    loop = asyncio.get_event_loop()
    await loop.run_in_executor(None, init_databases)

    async with bot:
        await load_all_cogs()
        # Refresh admin IDs after all cogs load — ensures config.json IDs are live
        from cogs.admin.admin import _refresh_admin_ids
        _refresh_admin_ids()
        log.info("✅  Admin IDs refreshed from config.json")
        await bot.start(token)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        log.info("Bot shutting down…")
        close_databases()
