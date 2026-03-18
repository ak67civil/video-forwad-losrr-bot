import os
import asyncio
from pyrogram import Client, filters

# Heroku Config Vars
API_ID = int(os.environ.get("API_ID", "33401543"))
API_HASH = os.environ.get("API_HASH", "7cdea5bbc8bd991b4a49807ce86")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

# Client Setup
app = Client(
    "LoserBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    in_memory=True
)

@app.on_message(filters.command("start") & filters.private)
async def start(client, message):
    await message.reply_text("💪 **Bhai! Bot ab Zinda hai!**\n\nAb ye crash nahi hoga, loop fix kar diya hai.")

@app.on_message(filters.command("id"))
async def get_id(client, message):
    await message.reply_text(f"👤 Your ID: `{message.from_user.id}`")

# --- NO-CRASH RUNNER ---
async def run_bot():
    async with app:
        print("🚀 BOT STARTED SUCCESSFULLY!")
        await asyncio.Event().wait()

if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        loop.run_until_complete(run_bot())
    except KeyboardInterrupt:
        pass
        
