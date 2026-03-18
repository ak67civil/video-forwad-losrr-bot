# 🛡️ Loser Premium Forwarder v4.0
**The Most Powerful & High-Speed Telegram Forwarder with Zero-Miss Technology.**

---

### 🌟 Key Features
* ⚡ **Zero-Miss Technology**: Ensures every single video and document is forwarded without any loss.
* 🏷️ **Auto-Captioning**: Automatically adds "**Forwarded By: Loser**" to every post.
* 💎 **Premium Management**: Built-in `/add` and `/remove` system for controlled user access.
* 📊 **Real-time Logging**: All activities are logged directly to your private `LOG_CHANNEL`.
* 🚀 **Asynchronous Engine**: Fully optimized for Python 3.14 and high-performance servers.

---

### 🚀 User Commands (Explaination)
| Command | Description |
| :--- | :--- |
| `/start` | Check if the bot is alive and view the help menu. |
| `/id` | Get your unique Telegram ID (ID Checker). |
| `/live` | **Live Forward**: Automatically forwards new posts as they arrive. |
| `/batch` | **Batch Forward**: Forwards old posts from a specific range/link. |
| `/stop` | Instantly stop any ongoing forwarding process. |
| `/cancel` | Cancel the current setup or operation. |

---

### 👑 Owner/Admin Commands
* `/add [UserID] [Days]` - Grant premium access to a user for a specific time.
* `/remove [UserID]` - Revoke premium access from a user.
* `/user` - View the complete list of all premium users.
* `/broadcast` - Send a message to all users in the database.

---



### 🛠️ Deployment Instructions
1. **GitHub**: Upload `main.py`, `requirements.txt`, `Procfile`, and `README.md`.
2. **Heroku Config Vars**: Fill in the following mandatory variables:
   - `API_ID` & `API_HASH` (From my.telegram.org)
   - `BOT_TOKEN` (From @BotFather)
   - `MONGO_DB_URI` (Your MongoDB Link)
   - `OWNER_ID` (Your Telegram ID)
   - `LOG_CHANNEL` (Your Private Log Channel ID)
3. **Resources**: Go to the Heroku dashboard and turn **ON** the `worker` dyno.

---
**Developed with ❤️ by Loser**
