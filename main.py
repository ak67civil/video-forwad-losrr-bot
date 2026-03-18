import os
import asyncio
from pyrogram import Client, filters, errors
from motor.motor_asyncio import AsyncIOMotorClient
from datetime import datetime, timedelta

# --- CONFIGS ---
API_ID = int(os.environ.get("API_ID", "33401543"))
API_HASH = os.environ.get("API_HASH", "7cdea5bbc8bd991b4a49807ce86")
BOT_TOKEN = os.environ.get("BOT_TOKEN")
MONGO_DB_URI = os.environ.get("MONGO_DB_URI")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-100...")) # Apna ID dalo
OWNER_ID = int(os.environ.get("OWNER_ID", "0"))

# Database Setup
db_client = AsyncIOMotorClient(MONGO_DB_URI)
db = db_client["LoserForwarderDB"]
users = db["premium_users"]

app = Client("LoserForwarder", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# --- MIDDLEWARE: Premium Check ---
async def is_premium(user_id):
    if user_id == OWNER_ID: return True
    user = await users.find_one({"user_id": user_id})
    return user and user["expiry"] > datetime.now()

# --- USER COMMANDS ---
@app.on_message(filters.command("start"))
async def start(client, message):
    is_p = await is_premium(message.from_user.id)
    text = (
        "🛡️ **Loser Premium Forwarder v4.0**\n\n"
        "🚀 **Commands Menu:**\n"
        "🔹 /start - Bot details aur help menu\n"
        "🔹 /id - Apna ya kisi chat ka ID nikalne ke liye\n"
        "🔹 /live - Naye posts ko turant forward karne ke liye\n"
        "🔹 /batch - Purane posts ko range ke hisab se forward karein\n"
        "🔹 /stop - Kisi bhi chalti process ko rokne ke liye\n"
        "🔹 /cancel - Current setup cancel karne ke liye\n\n"
        f"💎 **Premium Status:** {'Activated ✅' if is_p else 'No Access ❌'}\n"
        "✨ *High-speed forwarding with zero media miss!*"
    )
    await message.reply_text(text)

@app.on_message(filters.command("id"))
async def get_id(client, message):
    await message.reply_text(f"👤 **Your ID:** `{message.from_user.id}`\n👥 **Chat ID:** `{message.chat.id}`")

# --- OWNER/ADMIN COMMANDS ---
@app.on_message(filters.command("add") & filters.user(OWNER_ID))
async def add_user(client, message):
    try:
        args = message.text.split()
        u_id, days = int(args[1]), int(args[2])
        expiry = datetime.now() + timedelta(days=days)
        await users.update_one({"user_id": u_id}, {"$set": {"expiry": expiry}}, upsert=True)
        await message.reply_text(f"✅ User `{u_id}` added for {days} days.")
        if LOG_CHANNEL:
            await client.send_message(LOG_CHANNEL, f"👤 **New Premium User:** `{u_id}`\n⏳ **Validity:** {days} Days")
    except:
        await message.reply_text("❌ Usage: `/add [UserID] [Days]`")

@app.on_message(filters.command("remove") & filters.user(OWNER_ID))
async def remove_user(client, message):
    try:
        u_id = int(message.text.split()[1])
        await users.delete_one({"user_id": u_id})
        await message.reply_text(f"❌ User `{u_id}` access removed.")
    except:
        await message.reply_text("❌ Usage: `/remove [UserID]`")

@app.on_message(filters.command("user") & filters.user(OWNER_ID))
async def list_users(client, message):
    cursor = users.find({})
    text = "👥 **Premium Users List:**\n\n"
    async for u in cursor:
        text += f"• `{u['user_id']}` (Exp: {u['expiry'].strftime('%d-%m-%Y')})\n"
    await message.reply_text(text or "No premium users found.")

@app.on_message(filters.command("broadcast") & filters.user(OWNER_ID))
async def broadcast(client, message):
    if not message.reply_to_message:
        return await message.reply_text("Reply to a message to broadcast!")
    m = await message.reply_text("🚀 Broadcasting...")
    count = 0
    async for user in users.find({}):
        try:
            await message.reply_to_message.copy(user["user_id"])
            count += 1
        except: pass
    await m.edit(f"✅ Broadcast Done to {count} users.")

# --- FORWARDING LOGIC (With Auto-Caption & No-Miss) ---
@app.on_message((filters.video | filters.document | filters.photo) & ~filters.forwarded)
async def handle_forwarding(client, message):
    if not await is_premium(message.from_user.id): return
    
    # Custom Caption with 'Loser' Name
    original_caption = message.caption or ""
    new_caption = f"{original_caption}\n\n🎬 **Forwarded By: Loser**"
    
    # Destination logic for Batch/Live (Assuming DEST_ID is set in DB)
    # yahan aapka destination chat id aayega
    try:
        # Example forward (logic to be connected with /live)
        # await message.copy(chat_id=DEST_CHAT, caption=new_caption)
        pass
    except Exception as e:
        print(f"Error: {e}")

# --- STARTUP HANDLER ---
async def start_bot():
    try:
        await app.start()
        print("🚀 LOSER FORWARDER IS ONLINE!")
        if LOG_CHANNEL:
            await app.send_message(LOG_CHANNEL, "✅ **Forwarder Bot is now Online & Strong!**")
        await asyncio.Event().wait()
    except errors.FloodWait as e:
        await asyncio.sleep(e.value)
        await start_bot()

if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(start_bot())
