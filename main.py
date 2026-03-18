from pyrogram import Client, filters

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

SOURCE_CHANNEL = int(os.environ.get("SOURCE_CHANNEL"))
TARGET_CHANNEL = int(os.environ.get("TARGET_CHANNEL"))
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL"))

app = Client(
    "forward-bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.command("start") & filters.private)
async def start(client, message):
    await message.reply_text("✅ Bot is running perfectly!")

@app.on_message(filters.chat(SOURCE_CHANNEL))
async def auto_forward(client, message):
    try:
        await message.copy(TARGET_CHANNEL)
        await message.copy(LOG_CHANNEL)
        print("Forwarded")
    except Exception as e:
        print(e)

app.run()
