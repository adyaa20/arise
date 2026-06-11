"""
database.py — Solo Leveling Discord Bot
========================================
Dual-database architecture:
  • MongoDB Atlas  → Player data (hunters, stats, inventory, quests, guilds, etc.)
  • SQLite (local) → Bot data  (images, emojis, trivia questions, config, etc.)
"""

import os
import sqlite3
import logging
from contextlib import contextmanager
from datetime import datetime
from pathlib import Path
from typing import Optional

from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.errors import ConnectionFailure

log = logging.getLogger("database")

# ══════════════════════════════════════════════
#  SECTION 1 — MongoDB Atlas  (Player Data)
# ══════════════════════════════════════════════

MONGO_URI = os.getenv(
    "MONGO_URI",
    "mongodb+srv://Sakuuu:Saku%4011020@cluster0.vepzxe3.mongodb.net/sample_mflix"
    "?retryWrites=true&w=majority&appName=Cluster0",
)
MONGO_DB = os.getenv("MONGO_DB", "sample_mflix")


class MongoDB:
    _client: Optional[MongoClient] = None

    @classmethod
    def connect(cls) -> None:
        if cls._client is not None:
            return
        try:
            cls._client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=10_000, tlsInsecure=True)
            cls._client.admin.command("ping")
            log.info("✅  Connected to MongoDB Atlas (%s)", MONGO_DB)
        except ConnectionFailure as exc:
            log.critical("❌  MongoDB connection failed: %s", exc)
            raise

    @classmethod
    def disconnect(cls) -> None:
        if cls._client:
            cls._client.close()
            cls._client = None
            log.info("MongoDB connection closed.")

    @classmethod
    def col(cls, name: str) -> Collection:
        if cls._client is None:
            cls.connect()
        return cls._client[MONGO_DB][name]


# ── Player CRUD helpers ──────────────────────────────────────────────────────

# Base stats and start rewards — kept in sync with player_cog.py
_BASE_STATS = {
    "hp": 800, "mp": 200,
    "atk": 130, "def": 50,
    "prec": 15, "spd": 15,
}
_START_COINS = 500
_START_KEYS  = 1


def create_player(discord_id: int, username: str) -> dict:
    player = {
        "discord_id":       discord_id,
        "username":         username,
        "rank":             "E",
        "level":            1,
        "xp":               0,
        "skill_points":     0,
        **_BASE_STATS,
        "max_hp":           _BASE_STATS["hp"],
        "max_mp":           _BASE_STATS["mp"],
        "gold":             _START_COINS,
        "mana_crystals":    0,
        "gate_keys":        _START_KEYS,
        "national_level":   False,
        "exam_taken_today": False,
        "exam_date":        None,
        "monsters_killed":  0,
        "gates_cleared":    0,
        "daily_streak":     0,
        "last_daily":       None,
        "inventory":        [],
        "skills":           [],
        "guild_id":         None,
        "titles":           [],
        "awakened_at":      datetime.utcnow().strftime("%Y-%m-%d"),
        "created_at":       datetime.utcnow(),
        "updated_at":       datetime.utcnow(),
    }
    result = MongoDB.col("players").insert_one(player)
    player["_id"] = result.inserted_id
    log.info("New player created: %s (%d)", username, discord_id)
    return player


def get_player(discord_id: int) -> Optional[dict]:
    return MongoDB.col("players").find_one({"discord_id": discord_id})


def update_player(discord_id: int, fields: dict) -> bool:
    fields["updated_at"] = datetime.utcnow()
    result = MongoDB.col("players").update_one(
        {"discord_id": discord_id},
        {"$set": fields},
    )
    return result.modified_count > 0


def add_item_to_inventory(discord_id: int, item: dict) -> bool:
    result = MongoDB.col("players").update_one(
        {"discord_id": discord_id},
        {"$push": {"inventory": item}, "$set": {"updated_at": datetime.utcnow()}},
    )
    return result.modified_count > 0


def remove_item_from_inventory(discord_id: int, item_id: str) -> bool:
    result = MongoDB.col("players").update_one(
        {"discord_id": discord_id},
        {"$pull": {"inventory": {"item_id": item_id}}, "$set": {"updated_at": datetime.utcnow()}},
    )
    return result.modified_count > 0


def add_exp(discord_id: int, amount: int) -> dict:
    """Add XP to a player. Level-up logic is handled by player_cog.apply_level_up()."""
    result = MongoDB.col("players").update_one(
        {"discord_id": discord_id},
        {"$inc": {"xp": amount}, "$set": {"updated_at": datetime.utcnow()}},
    )
    return get_player(discord_id)


def delete_player(discord_id: int) -> bool:
    result = MongoDB.col("players").delete_one({"discord_id": discord_id})
    log.info("Player %d deleted from database.", discord_id)
    return result.deleted_count > 0


def add_coins(discord_id: int, amount: int) -> bool:
    """Add gold to a player's wallet."""
    result = MongoDB.col("players").update_one(
        {"discord_id": discord_id},
        {"$inc": {"gold": amount}, "$set": {"updated_at": datetime.utcnow()}},
    )
    return result.modified_count > 0


# ── Guild helpers ────────────────────────────────────────────────────────────

def create_guild(owner_id: int, name: str) -> dict:
    guild = {
        "owner_id":   owner_id,
        "name":       name,
        "level":      1,
        "members":    [owner_id],
        "bank":       0,
        "created_at": datetime.utcnow(),
    }
    result = MongoDB.col("guilds").insert_one(guild)
    guild["_id"] = result.inserted_id
    update_player(owner_id, {"guild_id": result.inserted_id})
    return guild


def get_guild(guild_id) -> Optional[dict]:
    from bson import ObjectId
    return MongoDB.col("guilds").find_one({"_id": ObjectId(str(guild_id))})


# ══════════════════════════════════════════════
#  SECTION 2 — SQLite  (Bot Data)
# ══════════════════════════════════════════════

SQLITE_PATH = os.getenv(
    "SQLITE_PATH",
    str(Path(__file__).resolve().parent / "bot_data.db"),
)


@contextmanager
def sqlite_conn():
    conn = sqlite3.connect(SQLITE_PATH)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def init_sqlite() -> None:
    ddl = """
    CREATE TABLE IF NOT EXISTS rank_images (
        rank        TEXT PRIMARY KEY,
        image_url   TEXT NOT NULL,
        thumbnail   BLOB
    );

    CREATE TABLE IF NOT EXISTS emojis (
        name        TEXT PRIMARY KEY,
        emoji_str   TEXT NOT NULL,
        is_custom   INTEGER DEFAULT 0,
        is_link     INTEGER DEFAULT 0
    );

    CREATE TABLE IF NOT EXISTS item_templates (
        item_id     TEXT PRIMARY KEY,
        name        TEXT NOT NULL,
        rarity      TEXT NOT NULL,
        type        TEXT NOT NULL,
        description TEXT,
        image_url   TEXT,
        base_stats  TEXT
    );

    CREATE TABLE IF NOT EXISTS skill_templates (
        skill_id    TEXT PRIMARY KEY,
        name        TEXT NOT NULL,
        rank        TEXT NOT NULL,
        mp_cost     INTEGER DEFAULT 0,
        description TEXT,
        image_url   TEXT
    );

    CREATE TABLE IF NOT EXISTS dungeon_templates (
        dungeon_id  TEXT PRIMARY KEY,
        name        TEXT NOT NULL,
        rank        TEXT NOT NULL,
        floors      INTEGER DEFAULT 10,
        image_url   TEXT,
        description TEXT
    );

    CREATE TABLE IF NOT EXISTS bot_config (
        key         TEXT PRIMARY KEY,
        value       TEXT NOT NULL,
        updated_at  TEXT DEFAULT (datetime('now'))
    );

    CREATE TABLE IF NOT EXISTS quest_templates (
        quest_id     TEXT PRIMARY KEY,
        title        TEXT NOT NULL,
        description  TEXT,
        type         TEXT NOT NULL DEFAULT 'daily',
        rank         TEXT NOT NULL DEFAULT 'E',
        reward_exp   INTEGER DEFAULT 0,
        reward_coins INTEGER DEFAULT 0,
        reward_items TEXT
    );

    CREATE TABLE IF NOT EXISTS trivia_questions (
        id          INTEGER PRIMARY KEY AUTOINCREMENT,
        category    TEXT NOT NULL,
        question    TEXT NOT NULL,
        option_a    TEXT NOT NULL,
        option_b    TEXT NOT NULL,
        option_c    TEXT NOT NULL,
        option_d    TEXT NOT NULL,
        answer      TEXT NOT NULL
    );
    """
    with sqlite_conn() as conn:
        conn.executescript(ddl)
    log.info("✅  SQLite tables initialised (%s)", SQLITE_PATH)


# ── Trivia helpers ───────────────────────────────────────────────────────────

def get_random_trivia(limit: int = 5) -> list:
    """Fetch random trivia questions from ALL categories mixed."""
    with sqlite_conn() as conn:
        rows = conn.execute(
            "SELECT * FROM trivia_questions ORDER BY RANDOM() LIMIT ?", (limit,)
        ).fetchall()
    return [dict(r) for r in rows]


def get_trivia_count() -> int:
    with sqlite_conn() as conn:
        return conn.execute("SELECT COUNT(*) FROM trivia_questions").fetchone()[0]


def add_trivia_question(category: str, question: str,
                        option_a: str, option_b: str,
                        option_c: str, option_d: str,
                        answer: str) -> None:
    """Insert a trivia question. answer should be 'A', 'B', 'C', or 'D'."""
    with sqlite_conn() as conn:
        conn.execute(
            "INSERT INTO trivia_questions (category, question, option_a, option_b, option_c, option_d, answer)"
            " VALUES (?, ?, ?, ?, ?, ?, ?)",
            (category, question, option_a, option_b, option_c, option_d, answer.upper()),
        )


# ── Quest helpers ────────────────────────────────────────────────────────────

def get_quests(type_: str = "daily") -> list:
    """Fetch all quest templates of a given type (daily/weekly)."""
    with sqlite_conn() as conn:
        rows = conn.execute(
            "SELECT * FROM quest_templates WHERE type = ? ORDER BY rank",
            (type_,)
        ).fetchall()
    return [dict(r) for r in rows]


# ── General SQLite helpers ───────────────────────────────────────────────────




def get_rank_image(rank: str) -> Optional[str]:
    with sqlite_conn() as conn:
        row = conn.execute("SELECT image_url FROM rank_images WHERE rank = ?", (rank,)).fetchone()
    return row["image_url"] if row else None


def upsert_rank_image(rank: str, image_url: str) -> None:
    with sqlite_conn() as conn:
        conn.execute(
            "INSERT INTO rank_images (rank, image_url) VALUES (?, ?)"
            " ON CONFLICT(rank) DO UPDATE SET image_url = excluded.image_url",
            (rank, image_url),
        )


def get_item_template(item_id: str) -> Optional[dict]:
    with sqlite_conn() as conn:
        row = conn.execute("SELECT * FROM item_templates WHERE item_id = ?", (item_id,)).fetchone()
    return dict(row) if row else None


def get_bot_config(key: str, default=None):
    with sqlite_conn() as conn:
        row = conn.execute("SELECT value FROM bot_config WHERE key = ?", (key,)).fetchone()
    return row["value"] if row else default


def set_bot_config(key: str, value: str) -> None:
    with sqlite_conn() as conn:
        conn.execute(
            "INSERT INTO bot_config (key, value) VALUES (?, ?)"
            " ON CONFLICT(key) DO UPDATE SET value = excluded.value, updated_at = datetime('now')",
            (key, value),
        )


# ══════════════════════════════════════════════
#  SECTION 3 — Initialisation
# ══════════════════════════════════════════════

def init_databases() -> None:
    MongoDB.connect()
    init_sqlite()
    from seeds import run_seeds
    run_seeds()
    MongoDB.col("players").create_index("discord_id", unique=True)
    MongoDB.col("guilds").create_index("name", unique=True)
    log.info("🗡️  Solo Leveling DB ready — MongoDB Atlas + SQLite online.")


def close_databases() -> None:
    MongoDB.disconnect()
    log.info("Databases closed cleanly.")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    init_databases()
    print("Trivia count:", get_trivia_count())
    close_databases()
    print("✅  All smoke tests passed.")