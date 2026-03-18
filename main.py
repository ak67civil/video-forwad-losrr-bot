import os
import asyncio
from pyrogram import Client, filters

# Heroku Config Vars
API_ID = int(os.environ.get("API_ID", "33401543"))
API_HASH = os.environ.get("API_HASH", "7cdea5bbc8bd991b4a49807ce86")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

app = Client(
    "LoserBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    in_memory=True
)

@app.on_message(filters.command("start") & filters.private)
async def start(client, message):
    await message.reply_text("💪 **Dekh Bhai! Bot ab Bilkul ON hai!**\n\nAb crash nahi hoga.")

# --- THE FIX FOR PYTHON 3.14 ---
async def main():
    async with app:
        print("🚀 BOT IS RUNNING!")
        await asyncio.Future() # Isse bot chalta rahega

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
        
