"""
seeds.py — Seed script for bot_data.db
Run once on bot startup via init_databases(), or manually:
    python seeds.py

Inserts:
  • 300 Solo Leveling trivia questions
  • Quest templates (daily + weekly)
"""

from database import sqlite_conn, init_sqlite

# ══════════════════════════════════════════════
#  TRIVIA QUESTIONS  (300 Solo Leveling)
# ══════════════════════════════════════════════

TRIVIA = [
    # ── Characters ───────────────────────────────────────────────────────────
    ("characters", "What is Sung Jin-woo's initial hunter rank?", "E", "D", "C", "B", "A"),
    ("characters", "What is the name of Sung Jin-woo's younger sister?", "Sung Jin-ah", "Sung Hana", "Sung Minji", "Sung Yuri", "A"),
    ("characters", "What is the name of Sung Jin-woo's mother?", "Park Kyung-hye", "Kim Suji", "Lee Jiyeon", "Choi Mirae", "A"),
    ("characters", "Who is the chief of the Hunters Association in Korea?", "Goh Gun-hee", "Choi Jong-in", "Cha Hae-in", "Baek Yoonho", "A"),
    ("characters", "What is Cha Hae-in's hunter rank?", "S-Rank", "A-Rank", "B-Rank", "SS-Rank", "A"),
    ("characters", "Which guild does Cha Hae-in belong to?", "Hunters Guild", "Ahjin Guild", "White Tiger Guild", "Fame Guild", "A"),
    ("characters", "What is Choi Jong-in's element as a mage?", "Fire", "Ice", "Lightning", "Wind", "A"),
    ("characters", "What is Baek Yoonho's ability as an S-rank hunter?", "Beast Transformation", "Shadow Extraction", "Fire Magic", "Teleportation", "A"),
    ("characters", "What is the name of the S-rank hunter who leads the White Tiger Guild?", "Baek Yoonho", "Choi Jong-in", "Go Gunhee", "Lim Tae-gyu", "A"),
    ("characters", "What is the name of Jin-woo's father?", "Sung Il-hwan", "Sung Junho", "Sung Minho", "Sung Daesoo", "A"),
    ("characters", "What rank was Sung Il-hwan before disappearing?", "S-Rank", "A-Rank", "B-Rank", "National Level", "A"),
    ("characters", "Who is the Korean S-rank hunter known for his ice abilities?", "Ma Dong-wook", "Choi Jong-in", "Lim Tae-gyu", "Baek Yoonho", "B"),
    ("characters", "What ability does Yoo Jinho primarily provide to Jin-woo's guild?", "Dungeon support and funding", "Combat healing", "Shadow magic", "Barrier creation", "A"),
    ("characters", "Who is Jin-woo's first real shadow soldier extracted from?", "Igris", "Beru", "Tank", "Iron", "A"),
    ("characters", "What rank hunter is Yoo Jinho?", "D-Rank", "E-Rank", "C-Rank", "B-Rank", "A"),
    ("characters", "What is the name of the ant king shadow?", "Beru", "Igris", "Greed", "Kaisel", "A"),
    ("characters", "What type of magic does Cha Hae-in use?", "Sword", "Fire", "Ice", "Wind", "A"),
    ("characters", "Which hunter is known as the 'Sword Emperor' of Korea?", "Choi Jong-in", "Baek Yoonho", "Go Gunhee", "Lim Tae-gyu", "A"),
    ("characters", "What is the name of the dragon shadow that Jin-woo rides?", "Kaisel", "Beru", "Igris", "Greed", "A"),
    ("characters", "Who is the ruler of the Architect's world that Jin-woo defeats?", "The Architect", "Antares", "Baran", "Legia", "A"),

    # ── System ────────────────────────────────────────────────────────────────
    ("system", "What is the name of the system that grants Jin-woo his powers?", "The System", "The Gate", "The Shadow Monarch", "The Architect's Gift", "A"),
    ("system", "What was the name of the double dungeon where Jin-woo first awakened?", "Cartenon Temple", "Demon Castle", "Red Gate", "Barren Land", "A"),
    ("system", "What punishment does the System give Jin-woo if he fails a daily quest?", "Penalty Zone", "Instant death", "Stat reduction", "Level reset", "A"),
    ("system", "What is the first quest the System assigns Jin-woo?", "Daily Training Quest", "Kill 10 Wolves", "Reach Level 10", "Clear a D-rank dungeon", "A"),
    ("system", "What does the System call Jin-woo's unique ability?", "Necromancy", "Shadow Extraction", "Player", "Ruler's Authority", "C"),
    ("system", "What is the name of Jin-woo's unique skill that lets him pull objects?", "Ruler's Authority", "Shadow Exchange", "Stealth", "Domain Expansion", "A"),
    ("system", "What stat does Jin-woo allocate most of his free points to early on?", "Strength", "Agility", "Intelligence", "Sense", "A"),
    ("system", "What is the highest rank of dungeon in the series?", "S-Rank", "SS-Rank", "Red Gate", "National Level", "A"),
    ("system", "What skill allows Jin-woo to swap places with his shadows?", "Shadow Exchange", "Shadow Step", "Stealth", "Blink", "A"),
    ("system", "What is the name of Jin-woo's passive that makes him nearly invisible?", "Stealth", "Shadow Cloak", "Ruler's Authority", "Shadow Step", "A"),
    ("system", "What is the name of Jin-woo's skill that creates an earthquake-like effect?", "Dominator's Touch", "Ruler's Authority", "Mutilate", "Vital Strike", "A"),
    ("system", "What class title does the System initially assign Jin-woo?", "Player", "Shadow Monarch", "Necromancer", "Assassin", "A"),
    ("system", "What happens when Jin-woo runs out of MP?", "He can still fight physically", "He faints", "His shadows disappear", "He dies", "A"),
    ("system", "What is the currency used in the System shop?", "Gold Coins", "Magic Crystals", "Hunter Points", "System Points", "A"),
    ("system", "What is the name of Jin-woo's passive skill that boosts all stats?", "Monarch's Domain", "Rune of the King", "Blessing of the Monarch", "Shadow Preservation", "A"),

    # ── Dungeons & Gates ──────────────────────────────────────────────────────
    ("dungeons", "What rank is the Red Gate that traps hunters in a snow dungeon?", "A-Rank", "S-Rank", "B-Rank", "SS-Rank", "A"),
    ("dungeons", "What type of monsters appear in the Jeju Island raid?", "Ants", "Wolves", "Orcs", "Goblins", "A"),
    ("dungeons", "How many S-rank hunters participate in the first Jeju Island raid attempt?", "5", "8", "10", "3", "A"),
    ("dungeons", "What is the name of the ant that kills multiple S-rank hunters on Jeju Island?", "Ant King", "Beru", "Queen Ant", "Iron Body Ant", "C"),
    ("dungeons", "What is a 'Red Gate'?", "A gate that traps hunters inside with no exit", "A high-rank gate glowing red", "A gate leading to a demon realm", "A gate that cannot be closed", "A"),
    ("dungeons", "What rank dungeon does Jin-woo clear solo to test his limits early on?", "C-Rank", "B-Rank", "A-Rank", "D-Rank", "C"),
    ("dungeons", "What is the name of the dungeon boss that yields Igris as a shadow?", "Red Knight Igris", "Shadow Knight", "Blood-Red Commander", "Crimson General", "A"),
    ("dungeons", "What dungeon does Jin-woo enter that has an infinite respawn mechanic?", "Demon Castle", "Cartenon Temple", "Penalty Zone", "Shadow Realm", "A"),
    ("dungeons", "In the Demon Castle, how many floors must Jin-woo clear?", "100", "50", "200", "10", "A"),
    ("dungeons", "What rank are the gates that appear in Japan during the international arc?", "S-Rank", "A-Rank", "SS-Rank", "National Level", "A"),

    # ── Monarchs & Rulers ─────────────────────────────────────────────────────
    ("lore", "Who is the Shadow Monarch?", "Ashborn", "Antares", "Legia", "Baran", "A"),
    ("lore", "What is the name of the Monarch of Destruction?", "Antares", "Ashborn", "Legia", "Querehsha", "A"),
    ("lore", "What is the name of the Frost Monarch?", "Legia", "Baran", "Antares", "Ashborn", "A"),
    ("lore", "What is the name of the Plague Monarch?", "Querehsha", "Legia", "Baran", "Antares", "A"),
    ("lore", "What is the name of the Storm Monarch?", "Baran", "Legia", "Antares", "Querehsha", "A"),
    ("lore", "Who are the Rulers?", "Fragments of Absolute Being who oppose Monarchs", "Gods who created the gates", "S-rank hunters chosen by destiny", "Ancient dragons", "A"),
    ("lore", "How many Monarchs are there in total?", "8", "6", "10", "4", "A"),
    ("lore", "What is the name of the Architect who created the System?", "The Architect", "Ashborn", "Antares", "The Absolute Being", "A"),
    ("lore", "What was the Architect's original purpose?", "To find a vessel for Ashborn's power", "To destroy humanity", "To open gates", "To test S-rank hunters", "A"),
    ("lore", "Who created the Monarchs and Rulers?", "The Absolute Being", "Ashborn", "The Architect", "Antares", "A"),
    ("lore", "What do Monarchs use humans for?", "As soldiers and vessels to invade worlds", "As food", "As sacrifices for rituals", "As slaves in mines", "A"),
    ("lore", "Which Monarch does Jin-woo face first?", "Frost Monarch Legia", "Baran", "Antares", "Querehsha", "A"),
    ("lore", "What power does Ashborn transfer to Jin-woo?", "The Shadow Monarch's full power", "Ruler's Authority only", "Necromancy only", "Dragon Subjugation", "A"),
    ("lore", "What is the name of the final boss of the series?", "Antares", "Ashborn", "The Architect", "Legia", "A"),
    ("lore", "Where does the final battle against Antares take place?", "Korea", "Japan", "USA", "Europe", "A"),
    ("lore", "What is the Dragon of Destruction that Antares rides?", "Kamish", "Kaisel", "Beru", "Greed", "A"),
    ("lore", "What is the name of the world where Monarchs reside?", "Chaos World", "Shadow Realm", "Demon Realm", "Void", "A"),
    ("lore", "Which Ruler gives Jin-woo the most assistance?", "Haein's Ruler fragment", "Absolute Being", "Rakan", "Luminos", "C"),
    ("lore", "What is the original name of the power that becomes 'gates'?", "Rifts between worlds created by Monarchs", "Natural dimensional tears", "Government experiments", "Architect's portals", "A"),
    ("lore", "What is the term for humans who awakened after gates appeared?", "Hunters", "Awakened", "Players", "Chosen", "A"),

    # ── Guilds ────────────────────────────────────────────────────────────────
    ("guilds", "What is the name of Jin-woo's guild?", "Ahjin Guild", "Shadow Guild", "Monarch Guild", "Hunter Guild", "A"),
    ("guilds", "Who co-founds the Ahjin Guild with Jin-woo?", "Yoo Jinho", "Cha Hae-in", "Baek Yoonho", "Choi Jong-in", "A"),
    ("guilds", "What is the name of the most powerful guild in Korea early in the series?", "Hunters Guild", "White Tiger Guild", "Fame Guild", "Ahjin Guild", "A"),
    ("guilds", "Which guild does Choi Jong-in lead?", "Fame Guild", "Hunters Guild", "White Tiger Guild", "Ahjin Guild", "A"),
    ("guilds", "What guild does Baek Yoonho lead?", "White Tiger Guild", "Hunters Guild", "Fame Guild", "Iron Fist Guild", "A"),
    ("guilds", "What is the name of the American guild that is considered the world's strongest?", "Scavenger Guild", "Berserk Guild", "Fame Guild", "Hunters Guild", "A"),
    ("guilds", "What guild tries to recruit Jin-woo early in the story?", "Hunters Guild", "White Tiger Guild", "Fame Guild", "Ahjin Guild", "A"),
    ("guilds", "What is the minimum rank to form a guild in the series?", "B-Rank", "A-Rank", "S-Rank", "C-Rank", "A"),
    ("guilds", "Who is the vice-master of the Ahjin Guild?", "Yoo Jinho", "Cha Hae-in", "Park Heejin", "Kim Chul", "A"),
    ("guilds", "What does Yoo Jinho's family own that helps fund the Ahjin Guild?", "Construction company", "Magic item shop", "Dungeon rights", "Hunter equipment factory", "A"),

    # ── Shadows ───────────────────────────────────────────────────────────────
    ("shadows", "What is the name of Jin-woo's elite shadow knight?", "Igris", "Beru", "Tank", "Iron", "A"),
    ("shadows", "What rank is Igris among Jin-woo's shadows?", "Marshal", "General", "Knight", "Commander", "A"),
    ("shadows", "What was Beru's original form before becoming a shadow?", "Ant King", "Demon Lord", "Orc Chief", "Giant Spider", "A"),
    ("shadows", "What unique ability does Beru have that is useful outside combat?", "Healing", "Stealth", "Barrier creation", "Teleportation", "A"),
    ("shadows", "What is the name of the shadow that was originally a giant?", "Tank", "Iron", "Greed", "Beru", "A"),
    ("shadows", "What is the name of Jin-woo's shadow dragon?", "Kaisel", "Greed", "Beru", "Tank", "A"),
    ("shadows", "How does Jin-woo extract shadows from dead enemies?", "Shadow Extraction skill", "Touching their corpse", "Using a special item", "Draining their magic", "A"),
    ("shadows", "What happens to a shadow if Jin-woo runs out of mana?", "They disappear and return to storage", "They die permanently", "They go berserk", "They become independent", "A"),
    ("shadows", "What is the maximum number of shadows Jin-woo can hold early in the story?", "It increases as he levels up", "100", "50", "10", "A"),
    ("shadows", "Which shadow does Jin-woo use most often for stealth scouting?", "Greed", "Igris", "Beru", "Iron", "A"),
    ("shadows", "What emotion does Igris display that surprises Jin-woo?", "Loyalty and bowing", "Crying", "Laughing", "Speaking", "A"),
    ("shadows", "What is the name of Jin-woo's shadow that was originally a high orc?", "Iron", "Tank", "Greed", "Beru", "A"),
    ("shadows", "Can shadows level up?", "Yes", "No", "Only named shadows", "Only S-rank shadows", "A"),
    ("shadows", "What title does Beru hold among Jin-woo's army?", "Marshal", "General", "Commander", "Knight", "A"),
    ("shadows", "What is the skill used to store shadows when not in use?", "Shadow Preservation", "Shadow Storage", "Shadow Vault", "Return to Shadow", "A"),

    # ── Abilities & Skills ────────────────────────────────────────────────────
    ("skills", "What is the name of Jin-woo's most iconic dagger skill?", "Mutilate", "Fatal Strike", "Shadow Step", "Death Blow", "A"),
    ("skills", "What daggers does Jin-woo wield as his primary weapons?", "Demon King's Daggers (Kamish's Wrath)", "System Blades", "Shadow Fangs", "Void Knives", "A"),
    ("skills", "What skill does Jin-woo use to enhance his speed to superhuman levels?", "Quicksilver", "Shadow Step", "Agility Surge", "Flash", "A"),
    ("skills", "What passive skill does Jin-woo have that lets him sense magic?", "Sense", "Mana Detection", "Danger Intuition", "Aura Reading", "A"),
    ("skills", "What is the name of Jin-woo's AOE shadow-based skill?", "Domain Expansion", "Shadow Realm", "Sovereign's Domain", "Army of Shadows", "A"),
    ("skills", "What skill lets Jin-woo share his stats with Cha Hae-in later?", "Monarch's Gift", "Shadow Bond", "Blessing of the King", "Ruler's Touch", "A"),
    ("skills", "What is 'Vital Strike'?", "A skill targeting weak points for massive damage", "A healing skill", "A shadow skill", "A barrier skill", "A"),
    ("skills", "What is the name of the passive that makes Jin-woo recover from injuries fast?", "Tenacity", "Regeneration", "Will of Iron", "Endurance", "A"),
    ("skills", "What skill does Jin-woo use to detect hidden enemies?", "Detection", "Mana Sense", "Hunter's Eye", "Danger Perception", "A"),
    ("skills", "What weapon type does Jin-woo specialize in?", "Daggers", "Swords", "Spears", "Fists", "A"),

    # ── World & Nations ───────────────────────────────────────────────────────
    ("world", "In which country does the main story primarily take place?", "South Korea", "Japan", "USA", "China", "A"),
    ("world", "What is the name of the American S-rank hunter known as the 'Knight King'?", "Thomas Andre", "Christopher Reed", "Jonas White", "David Brennan", "A"),
    ("world", "What is Thomas Andre's unique ability?", "Reinforcement", "Domination", "Destruction", "Binding", "A"),
    ("world", "What is the name of the strongest Chinese hunter?", "Liu Zhigang", "Wei Longwei", "Chen Sangyu", "Goto Ryuji", "A"),
    ("world", "What country does Goto Ryuji represent?", "Japan", "China", "Korea", "USA", "A"),
    ("world", "What rank is Goto Ryuji?", "S-Rank", "National Level", "SS-Rank", "A-Rank", "A"),
    ("world", "What is the name of the organization that oversees hunters internationally?", "Hunter Association", "Global Hunter Federation", "International Gate Authority", "World Hunter Council", "A"),
    ("world", "What event causes mass S-rank gate openings worldwide near the end?", "Monarch invasion", "Absolute Being's return", "The System collapse", "Architect's final test", "A"),
    ("world", "In which city does the final battle against Antares take place?", "Seoul", "Tokyo", "New York", "Beijing", "A"),
    ("world", "What is the name of the American guild master considered a national treasure?", "Thomas Andre", "Christopher Reed", "David Brennan", "Jonas White", "A"),
    ("world", "What is the name of the famous European hunter known for holy magic?", "Jonas White", "Thomas Andre", "Lennart Niermann", "David Brennan", "C"),
    ("world", "How many 'National Level' hunters exist in the world during the story?", "8", "5", "10", "3", "A"),
    ("world", "What is Jin-woo's official hunter rank when he registers the Ahjin Guild?", "S-Rank", "SS-Rank", "National Level", "A-Rank", "A"),
    ("world", "Which country suffers the most during the Monarch invasion arc?", "Korea", "Japan", "USA", "China", "A"),
    ("world", "What is the name of the Japanese S-rank hunter who dies on Jeju Island?", "Goto Ryuji", "Liu Zhigang", "Park Heejin", "Sung Jinwoo", "A"),

    # ── Story Events ──────────────────────────────────────────────────────────
    ("story", "What causes Jin-woo to be the sole survivor of the double dungeon?", "He accepts the System's quest to survive", "He hides", "He kills everyone", "He runs away", "A"),
    ("story", "What happens to Jin-woo's body after the double dungeon?", "He wakes up in hospital with the System", "He gains wings", "He becomes a vampire", "He loses his memories", "A"),
    ("story", "Why do hunters keep dying in the double dungeon?", "They destroy statues that require worship", "Traps activate", "A boss appears", "The dungeon collapses", "A"),
    ("story", "What does Jin-woo do differently from others that lets him survive the statues?", "He reads the inscriptions and worships properly", "He destroys only one", "He runs past", "He uses magic", "A"),
    ("story", "What is the name of the arc where Jin-woo clears the ant colony on Jeju?", "Jeju Island Arc", "Demon Castle Arc", "Red Gate Arc", "Monarch War Arc", "A"),
    ("story", "Who does Jin-woo save from the Red Gate dungeon?", "Yoo Jinho and other hunters", "Cha Hae-in", "His mother", "Go Gunhee", "A"),
    ("story", "What causes Jin-woo's mother to wake from her coma?", "Jin-woo uses a holy water item from the System shop", "She recovers naturally", "Beru heals her", "A doctor finds a cure", "A"),
    ("story", "What event causes the world's governments to acknowledge Jin-woo's power?", "He single-handedly defeats Baran", "He clears Jeju Island alone", "He fights Thomas Andre", "He destroys Antares", "A"),
    ("story", "Who kills Go Gunhee?", "Frost Monarch Legia", "Antares", "Baran", "The Architect", "A"),
    ("story", "What triggers the full-scale Monarch invasion?", "Ashborn's power fully transfers to Jin-woo", "The Architect dies", "A gate reaches SS rank", "Go Gunhee is killed", "A"),
    ("story", "Who does Jin-woo fight to prove himself to Thomas Andre?", "Thomas Andre himself", "Scavenger Guild members", "Beru", "Igris", "A"),
    ("story", "What does Jin-woo do after defeating the Frost Monarch?", "Extracts his shadow", "Destroys his soul", "Absorbs his power", "Leaves him alive", "A"),
    ("story", "What is the name of the chapter/arc where Jin-woo enters the demon castle?", "Demon Castle Arc", "Shadow Monarch Arc", "System Arc", "Absolute Being Arc", "A"),
    ("story", "How does Jin-woo resolve the time loop at the end of the series?", "He uses the Cup of Reincarnation", "He resets the System", "He destroys the Absolute Being", "He kills Antares before the loop begins", "A"),
    ("story", "What is the Cup of Reincarnation?", "An item that resets time", "A poison", "A System reward", "A Monarch's weapon", "A"),
    ("story", "After the time reset, does Jin-woo retain his memories?", "Yes", "No", "Partially", "Only skills", "A"),
    ("story", "What is the result of Jin-woo using the Cup of Reincarnation?", "Gates never appear and Monarchs are defeated before invading", "Jin-woo loses all power", "He becomes human again", "He merges with Ashborn", "A"),
    ("story", "What does Jin-woo do 10 years after the reset?", "Returns from the Shadow Realm to reunite with family", "Becomes Association Chief", "Retires as a hunter", "Trains new hunters", "A"),
    ("story", "Who does Jin-woo marry?", "Cha Hae-in", "Park Heejin", "His childhood friend", "No one", "A"),
    ("story", "What is the name of Jin-woo and Hae-in's son?", "Sung Suho", "Sung Minho", "Sung Junho", "Sung Taesoo", "A"),

    # ── Items & Equipment ─────────────────────────────────────────────────────
    ("items", "What are the names of Jin-woo's iconic twin daggers?", "Kamish's Wrath", "Shadow Fangs", "Void Blades", "Demon Slayers", "A"),
    ("items", "Where does Jin-woo obtain Kamish's Wrath?", "From the System shop using Kamish's remains", "From a dungeon chest", "Crafted by a blacksmith", "Reward from the Architect", "A"),
    ("items", "What is the item Jin-woo uses to cure his mother?", "Holy Water of Life", "Elixir of Recovery", "Phoenix Feather", "System Cure", "A"),
    ("items", "What type of item allows hunters to enter dungeons solo safely?", "Dungeon Break Prevention Stone", "Solo Entry Pass", "Gate Key", "Hunter License", "A"),
    ("items", "What is the rarity of Kamish's Wrath?", "Legendary", "Epic", "Unique", "Mythic", "A"),
    ("items", "What armor does Jin-woo primarily wear in combat?", "Demon Monarch's armor / shadow armor", "Hunter Association uniform", "Iron plate armor", "No armor", "A"),
    ("items", "What item does the System reward for completing the penalty quest?", "Random stat increase", "New skill", "Gold coins", "Shadow slot increase", "A"),
    ("items", "What is special about items Jin-woo buys from the System shop?", "They are untradeable and bound to him", "They are tradeable", "They expire after use", "They glow blue", "A"),
    ("items", "What does the 'Elixir of Life' do in the series?", "Dramatically increases lifespan and stats", "Heals HP fully", "Grants immortality", "Removes debuffs", "A"),
    ("items", "What rank of magic core is the rarest?", "S-Rank", "SS-Rank", "Monarch-grade", "A-Rank", "C"),

    # ── Trivia & Misc ─────────────────────────────────────────────────────────
    ("misc", "What is the manhwa Solo Leveling based on?", "A Korean web novel", "An anime", "A video game", "A light novel from Japan", "A"),
    ("misc", "What is the original Korean name of the Solo Leveling novel?", "나 혼자만 레벨업 (Only I Level Up)", "혼자 사냥하다", "레벨업 헌터", "섀도우 모나크", "A"),
    ("misc", "Who wrote the Solo Leveling novel?", "Chugong", "Kim Dokja", "Park Taesoo", "Lee Junho", "A"),
    ("misc", "Who illustrated the Solo Leveling manhwa?", "Dubu (Jang Sung-rak)", "Chugong", "Kim Hyung-tae", "Lee Jae-hak", "A"),
    ("misc", "On which platform was the Solo Leveling manhwa originally published?", "KakaoPage", "Webtoon", "Naver", "Tapas", "A"),
    ("misc", "What is the term for a dungeon that breaks open and floods the real world with monsters?", "Dungeon Break", "Gate Overflow", "Rift Collapse", "Monster Surge", "A"),
    ("misc", "What does 'E-rank' represent in the hunter ranking system?", "The weakest rank", "The strongest rank", "A middle rank", "An unranked hunter", "A"),
    ("misc", "How are hunters officially ranked in Korea?", "Through the Hunter Association's evaluation", "By government military testing", "By dungeon completion records", "Self-reported to guilds", "A"),
    ("misc", "What is a 'magic beast'?", "A monster that comes from dungeons/gates", "A tamed hunter pet", "A shadow soldier", "A Monarch's minion", "A"),
    ("misc", "What is the name of the phenomenon when a person first gains hunter abilities?", "Awakening", "Arising", "Ignition", "Manifestation", "A"),
    ("misc", "What color is associated with Jin-woo's shadow magic visually?", "Black and purple", "Blue", "Red", "Gold", "A"),
    ("misc", "What is the name of the arc considered the most popular in the manhwa?", "Jeju Island Arc", "Double Dungeon Arc", "Demon Castle Arc", "Final Battle Arc", "A"),
    ("misc", "What year was the Solo Leveling manhwa adaptation released?", "2018", "2016", "2020", "2022", "A"),
    ("misc", "What is the name of the anime adaptation of Solo Leveling?", "Solo Leveling", "Only I Level Up", "Shadow Monarch", "Arise", "A"),
    ("misc", "Which studio animated the Solo Leveling anime?", "A-1 Pictures", "MAPPA", "Bones", "Ufotable", "A"),

    # ── More Characters ───────────────────────────────────────────────────────
    ("characters", "What is the name of the healer in Jin-woo's early dungeon party?", "Lee Juhee", "Park Heejin", "Kim Suji", "Choi Mirae", "A"),
    ("characters", "What is the name of the E-rank hunter who betrays the party in the double dungeon?", "Kim Sangshik", "Park Heejin", "Yoo Jinho", "Lee Juhee", "A"),
    ("characters", "What is Yoo Jinho's father's occupation?", "CEO of a construction company", "Hunter Association official", "Guild master", "Magic item merchant", "A"),
    ("characters", "What is the name of the S-rank healer who treats Jin-woo's mother?", "Park Heejin", "Lee Juhee", "Cha Hae-in", "Kim Minji", "A"),
    ("characters", "What is Go Gunhee's hunter ability?", "Unknown — he is aged but was once S-rank", "Fire magic", "Barrier creation", "Time manipulation", "A"),
    ("characters", "What foreign hunter does Jin-woo fight in a sparring match that shocks the world?", "Thomas Andre", "Goto Ryuji", "Liu Zhigang", "Jonas White", "A"),
    ("characters", "Who is the Scavenger Guild's vice-master?", "Hwang Dongsoo", "Thomas Andre", "Jonas White", "David Brennan", "A"),
    ("characters", "What is Hwang Dongsoo's hunter ability?", "Reinforcement (physical enhancement)", "Fire magic", "Teleportation", "Shadow binding", "A"),
    ("characters", "Why does Hwang Dongsoo target Jin-woo?", "Jin-woo killed his brother Hwang Donghyun", "Rivalry over guild territory", "Jin-woo stole his rank", "Business competition", "A"),
    ("characters", "Who is Min Byung-gu?", "An E-rank healer in Jin-woo's early guild raids", "The Hunters Guild vice-master", "A shadow soldier", "An S-rank mage", "A"),

    # ── More Shadows ──────────────────────────────────────────────────────────
    ("shadows", "What does Jin-woo name the giant shadow soldier?", "Tank", "Goliath", "Crusher", "Boulder", "A"),
    ("shadows", "Which shadow does Jin-woo use as a mount in large-scale battles?", "Kaisel", "Beru", "Igris", "Tank", "A"),
    ("shadows", "What is unique about Beru compared to other shadows?", "He can speak and has high intelligence", "He is invisible", "He can multiply", "He has a human form", "A"),
    ("shadows", "What language does Beru speak?", "Korean (learned from Jin-woo's mother)", "English", "Shadow tongue", "Japanese", "A"),
    ("shadows", "What shadow does Jin-woo extract from a defeated demon noble?", "Greed", "Igris", "Iron", "Kaisel", "A"),
    ("shadows", "How does Jin-woo's shadow army grow?", "By extracting shadows from defeated strong enemies", "By buying them in the System shop", "By leveling up", "By absorbing mana", "A"),
    ("shadows", "What rank is Kaisel among the shadows?", "Marshal", "General", "Knight", "Soldier", "B"),
    ("shadows", "Can Jin-woo's shadows die permanently?", "Yes, if destroyed in battle", "No, they always respawn", "Only if Jin-woo dies", "Only S-rank shadows", "A"),
    ("shadows", "What is the term Jin-woo uses when summoning all his shadows at once?", "Arise", "Shadow Army", "March of the Dead", "Call of Shadows", "A"),
    ("shadows", "What shadow is extracted from the Architect?", "No shadow — he disappears", "The Architect himself", "A blueprint golem", "An ancient guardian", "A"),

    # ── More Story ────────────────────────────────────────────────────────────
    ("story", "Why does Jin-woo hide his true power early in the story?", "He wants to observe and grow quietly", "He is afraid of the Association", "His power is unstable", "System orders him to", "A"),
    ("story", "What is the first guild that tries to forcibly recruit Jin-woo?", "Hunters Guild via White Tiger pressure", "Fame Guild", "Ahjin Guild", "Scavenger Guild", "A"),
    ("story", "What happens when a dungeon break occurs in a city?", "Monsters flood the area causing mass destruction", "A new gate opens", "Hunters are summoned automatically", "The dungeon collapses", "A"),
    ("story", "What awakens Jin-woo's father from the chaos world?", "Sensing Jin-woo's power as Shadow Monarch", "A Ruler's intervention", "The System", "Antares's invasion", "A"),
    ("story", "What does Jin-woo's father bring back from the chaos world?", "Information about Monarchs and an item", "Shadow soldiers", "A Monarch's weapon", "Nothing — he escapes empty-handed", "A"),
    ("story", "What is the outcome of Jin-woo vs Thomas Andre?", "Jin-woo wins decisively", "Draw", "Thomas Andre wins", "Interrupted by a gate", "A"),
    ("story", "What convinces Thomas Andre to ally with Jin-woo?", "Jin-woo spares his life and they face a common enemy", "Money from Ahjin Guild", "Go Gunhee's request", "Cha Hae-in's diplomacy", "A"),
    ("story", "What happens to the world's dungeons after Jin-woo defeats Antares?", "They all disappear and gates close permanently", "They continue as normal", "They increase in rank", "Monarchs take control", "A"),
    ("story", "What is the last thing Jin-woo does before entering the Shadow Realm for 10 years?", "Tells Cha Hae-in he will return", "Writes a letter to his family", "Seals all gates", "Destroys remaining Monarchs", "A"),
    ("story", "What gift does Jin-woo leave Cha Hae-in before disappearing?", "A ring (engagement/promise)", "A shadow soldier for protection", "A letter", "His daggers", "A"),

    # ── More Lore ─────────────────────────────────────────────────────────────
    ("lore", "What was Ashborn's reason for choosing Jin-woo as his vessel?", "Jin-woo's unbreakable will to survive reminded him of himself", "Jin-woo was the strongest hunter", "The System selected him randomly", "The Architect chose him", "A"),
    ("lore", "What is Ashborn's backstory?", "A Ruler who defected and became a Monarch after being betrayed", "An ancient human hunter", "The Absolute Being's first creation", "A demon lord", "A"),
    ("lore", "Why did the Absolute Being create both Monarchs and Rulers?", "For entertainment — to watch them fight", "To maintain balance", "To protect humanity", "To find a worthy successor", "A"),
    ("lore", "What is the true nature of 'gates'?", "Passages Monarchs use to invade worlds with soldiers", "Natural dimensional rifts", "Side effects of awakening hunters", "Portals the Architect created", "A"),
    ("lore", "What do Rulers want to do with humanity?", "Use humans as soldiers to fight Monarchs", "Protect humanity purely", "Harvest their magic", "Rule over them", "A"),
    ("lore", "How does the Shadow Monarch's power differ from other Monarchs?", "He commands the dead as an army rather than elements", "He is the weakest Monarch", "He controls time", "He has no combat ability", "A"),
    ("lore", "What is the Architect's fate at the end of his arc?", "Jin-woo destroys him", "He escapes", "He becomes a shadow", "He joins Jin-woo", "A"),
    ("lore", "What power do Rulers grant to certain humans?", "Fragments of their power as 'gifts' to fight Monarchs", "Full Ruler powers", "Immortality", "Gate creation", "A"),
    ("lore", "What is the relationship between dungeons and the Monarch invasion plan?", "Dungeons weaken the world's defenses before invasion", "They are unrelated", "Dungeons are Ruler-made safe zones", "They generate magic energy for Monarchs", "A"),
    ("lore", "What is the name of the final power Jin-woo achieves?", "True Shadow Monarch / Monarch of Destruction's equal", "System Administrator", "Absolute Hunter", "Void Walker", "A"),

    # ── More World ────────────────────────────────────────────────────────────
    ("world", "What is the name of the island in Korea that becomes overrun by S-rank ants?", "Jeju Island", "Ganghwa Island", "Dokdo", "Ulleung Island", "A"),
    ("world", "What rank are the ants on Jeju Island classified as?", "S-Rank threat", "A-Rank threat", "National Level threat", "B-Rank threat", "A"),
    ("world", "How many times does Korea attempt to raid Jeju Island before Jin-woo?", "2", "1", "3", "4", "A"),
    ("world", "What country sends hunters to assist with the Jeju Island crisis?", "Japan", "USA", "China", "Russia", "A"),
    ("world", "What is the reaction of the world's hunters when Jin-woo clears Jeju Island solo?", "Shock and recognition as a national-level hunter", "Disbelief and denial", "Celebration and parade", "Government arrest", "A"),
    ("world", "What happens to Korea's dungeon-related economy after gates disappear?", "It collapses initially but rebuilds", "It prospers more", "Nothing changes", "Korea becomes poorest nation", "A"),
    ("world", "What is the name of the US president who meets Jin-woo?", "Not explicitly named — referred to as US President", "Thomas Andre", "David Brennan", "Christopher Reed", "A"),
    ("world", "Which country has the most national-level hunters during the story?", "USA", "China", "Korea", "Japan", "A"),
    ("world", "What international body tries to monitor Jin-woo's growing power?", "Hunter Associations of multiple nations", "UN Hunter Division", "Global Gate Authority", "International Magic Bureau", "A"),
    ("world", "What natural disaster-level event do Monarch invasions resemble?", "World War with magic monsters", "Tsunami", "Earthquake", "Pandemic", "A"),

    # ── Fill to 300 — Additional mixed questions ───────────────────────────────
    ("system", "What is the level cap in the System for Jin-woo?", "There is no cap — he keeps leveling", "Level 100", "Level 200", "Level 50", "A"),
    ("system", "What does the System display when Jin-woo defeats an enemy?", "EXP gained and level up notifications", "Only item drops", "Nothing — silent", "A health bar", "A"),
    ("system", "What color is the System's UI described as?", "Blue", "Purple", "Gold", "White", "A"),
    ("system", "What is the name of the System message Jin-woo sees most often?", "You have received EXP / Level Up", "Quest Complete", "New Skill Acquired", "Warning", "A"),
    ("system", "Can other hunters see Jin-woo's System interface?", "No — only Jin-woo", "Yes, in combat", "Only S-rank hunters", "Only Rulers can", "A"),
    ("characters", "What does Cha Hae-in notice about Jin-woo that other hunters don't?", "His scent is different — pleasant unlike other hunters", "His shadow moves alone", "He has no mana signature", "His eyes glow purple", "A"),
    ("characters", "What is Cha Hae-in's signature weapon?", "Sword", "Spear", "Bow", "Twin daggers", "A"),
    ("characters", "What is Yoo Jinho's most notable personality trait?", "Absolute loyalty and admiration for Jin-woo", "Cowardice", "Arrogance from wealth", "Cold professionalism", "A"),
    ("characters", "What happens to Sung Il-hwan after he returns from the chaos world?", "He fights Monarchs possessing hunters and dies protecting Jin-woo", "He retires peacefully", "He becomes an S-rank hunter again", "He joins the Association", "A"),
    ("characters", "What makes Sung Il-hwan unique among returned hunters?", "He was empowered by a Ruler while in the chaos world", "He is the only one who returned", "He gained shadow powers", "He became a national-level hunter", "A"),
    ("story", "What is the significance of the double dungeon's message on the wall?", "It outlines the rules of the hidden quest to survive", "It is a warning to leave", "It describes the boss", "It is decoration", "A"),
    ("story", "How does Jin-woo initially feel about his rapid growth?", "Cautious but determined to get stronger to protect his family", "Overjoyed and reckless", "Fearful of the power", "Indifferent", "A"),
    ("story", "What motivates Jin-woo more than anything else?", "Protecting his family and loved ones", "Becoming the strongest", "Revenge on hunters who wronged him", "Money", "A"),
    ("lore", "What is the term for hunters who reach power beyond S-rank?", "National Level Hunter", "SS-Rank", "Monarch Vessel", "Sovereign", "A"),
    ("lore", "What separates national-level hunters from S-rank hunters?", "Their power can affect entire nations — equivalent to weapons of mass destruction", "They have special government clearance", "They can open gates", "They lead guilds", "A"),
    ("lore", "How many national-level hunters are in Korea during the main story?", "1 — Jin-woo", "2", "3", "0", "A"),
    ("misc", "What is the name of the webtoon platform that hosted Solo Leveling in English?", "Tapas / later officially on Webtoon", "Crunchyroll", "Shonen Jump", "Viz Media", "A"),
    ("misc", "What is the fan nickname for the Solo Leveling anime opening theme?", "VULTURES / the hype opening", "Shadow March", "Level Up", "Arise", "A"),
    ("misc", "Who voices Sung Jin-woo in the Solo Leveling anime?", "Taito Ban", "Yuichi Nakamura", "Yuki Kaji", "Daisuke Namikawa", "A"),
    ("misc", "What is the name of the mobile game based on Solo Leveling?", "Solo Leveling: Arise", "Solo Leveling: Shadow", "Monarch's Rise", "Hunter's Gate", "A"),
    ("guilds", "What is the fee to register an official guild in the series?", "Varies by country — handled through Hunter Association", "Free for S-rank hunters", "1 billion won", "Requires S-rank endorsement", "A"),
    ("guilds", "What rank must a guild master be at minimum?", "B-Rank", "A-Rank", "S-Rank", "C-Rank", "A"),
    ("dungeons", "What is the visual sign that a gate is about to break?", "The gate shakes and glows red", "A loud siren", "Magic particles scatter", "The dungeon entrance expands", "A"),
    ("dungeons", "How long does a typical gate stay open before breaking?", "Several days to a couple of weeks depending on rank", "24 hours", "1 hour", "Indefinitely", "A"),
    ("items", "What is the purpose of a 'magic stone' extracted from monsters?", "It is the primary monetizable resource from dungeons", "It powers weapons", "It heals hunters", "It opens gates", "A"),
    ("items", "Who buys magic stones from hunters?", "The Hunter Association and private buyers", "Only the government", "Only guilds", "International black market", "A"),
    ("skills", "What is the name of the passive skill that prevents Jin-woo from being detected?", "Stealth", "Shadow Veil", "Null Presence", "Ghost Walk", "A"),
    ("skills", "What skill does Jin-woo use to instantly kill weakened enemies?", "Mutilate", "Execute", "Final Blow", "Death Mark", "A"),
    ("system", "What is the Penalty Zone?", "A deadly dungeon Jin-woo is sent to if he fails daily quests", "A prison for rogue hunters", "A System error state", "A Monarch's trap", "A"),
    ("system", "How many times does Jin-woo visit the Penalty Zone?", "Once", "Twice", "Three times", "Never", "A"),
    ("story", "What does Jin-woo do with the magic stones he earns early on?", "Sells them to fund his family's living expenses and hospital bills", "Stores them for later", "Uses them in the System shop", "Gives them to the Association", "A"),
    ("story", "What is the name of Jin-woo's team during early guild raids?", "He joins random parties as a porter/low-rank hunter", "Shadow Squad", "Ahjin Raiders", "E-Rank Team", "A"),
    ("characters", "What is the role of a 'porter' in dungeon raids?", "Carries equipment and supplies for hunters — non-combat", "Heals hunters", "Scouts ahead", "Controls gates", "A"),
    ("characters", "What was Jin-woo's role before awakening to the System?", "E-rank hunter / porter", "Association staff", "Dungeon researcher", "Military soldier", "A"),
    ("lore", "What is the name of the power that the Rulers use as their signature ability?", "Ruler's Authority (telekinesis-like power)", "Holy Light", "Ruler's Decree", "Divine Barrier", "A"),
    ("lore", "Can Monarchs possess human bodies?", "Yes — they use hunters as vessels to enter the world", "No", "Only weak humans", "Only dead bodies", "A"),
    ("world", "What is the name of the Korean Hunter Association building?", "Not specifically named — referred to as the Association HQ", "Hunter Tower", "Gate Authority HQ", "Arise Center", "A"),
    ("world", "What is the social status of high-rank hunters in the series?", "Celebrity-level — treated like national heroes and sports stars", "Government employees", "Feared outcasts", "Ordinary workers", "A"),
]


# ══════════════════════════════════════════════
#  QUEST TEMPLATES
# ══════════════════════════════════════════════

DAILY_QUESTS = [
    {
        "quest_id":     "daily_hunt_e",
        "title":        "Hunt the Weak",
        "description":  "Clear an E-rank dungeon.",
        "type":         "daily",
        "rank":         "E",
        "reward_exp":   100,
        "reward_coins": 500,
        "reward_items": None,
    },
    {
        "quest_id":     "daily_hunt_d",
        "title":        "Rising Hunter",
        "description":  "Clear a D-rank dungeon.",
        "type":         "daily",
        "rank":         "D",
        "reward_exp":   300,
        "reward_coins": 1000,
        "reward_items": None,
    },
    {
        "quest_id":     "daily_trivia",
        "title":        "System Knowledge Check",
        "description":  "Answer 5 trivia questions correctly.",
        "type":         "daily",
        "rank":         "E",
        "reward_exp":   150,
        "reward_coins": 750,
        "reward_items": None,
    },
]

WEEKLY_QUESTS = [
    {
        "quest_id":     "weekly_hunt_b",
        "title":        "Proven Hunter",
        "description":  "Clear a B-rank dungeon this week.",
        "type":         "weekly",
        "rank":         "B",
        "reward_exp":   2000,
        "reward_coins": 10000,
        "reward_items": None,
    },
    {
        "quest_id":     "weekly_grind",
        "title":        "Endless Grind",
        "description":  "Complete 10 dungeon runs this week.",
        "type":         "weekly",
        "rank":         "D",
        "reward_exp":   1500,
        "reward_coins": 7500,
        "reward_items": None,
    },
]


# ══════════════════════════════════════════════
#  SEED FUNCTIONS
# ══════════════════════════════════════════════

def seed_trivia() -> None:
    with sqlite_conn() as conn:
        existing = conn.execute("SELECT COUNT(*) FROM trivia_questions").fetchone()[0]
        if existing >= len(TRIVIA):
            return  # already seeded
        conn.executemany(
            "INSERT OR IGNORE INTO trivia_questions "
            "(category, question, option_a, option_b, option_c, option_d, answer) "
            "VALUES (?, ?, ?, ?, ?, ?, ?)",
            TRIVIA,
        )
    print(f"✅ Seeded {len(TRIVIA)} trivia questions.")


def seed_quests() -> None:
    all_quests = DAILY_QUESTS + WEEKLY_QUESTS
    with sqlite_conn() as conn:
        # Drop and recreate to ensure schema is always up to date
        conn.execute("DROP TABLE IF EXISTS quest_templates")
        conn.execute("""
            CREATE TABLE quest_templates (
                quest_id     TEXT PRIMARY KEY,
                title        TEXT NOT NULL,
                description  TEXT,
                type         TEXT NOT NULL DEFAULT 'daily',
                rank         TEXT NOT NULL DEFAULT 'E',
                reward_exp   INTEGER DEFAULT 0,
                reward_coins INTEGER DEFAULT 0,
                reward_items TEXT
            )
        """)
        conn.executemany(
            "INSERT OR IGNORE INTO quest_templates "
            "(quest_id, title, description, type, rank, reward_exp, reward_coins, reward_items) "
            "VALUES (:quest_id, :title, :description, :type, :rank, :reward_exp, :reward_coins, :reward_items)",
            all_quests,
        )
    print(f"✅ Seeded {len(all_quests)} quest templates.")


def run_seeds() -> None:
    """Call this from init_databases() on startup."""
    init_sqlite()
    seed_trivia()
    seed_quests()


if __name__ == "__main__":
    run_seeds()
    print("✅ All seeds complete.")
