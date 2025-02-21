import os
import json
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext, CallbackQueryHandler

# Load bot config from environment variables
CONFIG_FILE = "bot_config.json"

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    else:
        default_config = {
            "TOKEN": os.getenv("7202524149:AAGcqCLLW79Aw_dAk3e5ayLkBI9kUW-76tQ"),
            "OWNER_ID": int(os.getenv("OWNER_ID", 5787359348)),
            "DATABASE_URL": os.getenv("mongodb+srv://moviewala630:tbBtNRsvcYPYcRU5@cluster0.5ough.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"),
            "SUDO_USERS": json.loads(os.getenv("SUDO_USERS", "[]"))
        }
        with open(CONFIG_FILE, "w") as f:
            json.dump(default_config, f, indent=4)
        return default_config

config = load_config()
TOKEN = config["TOKEN"]
OWNER_ID = config["OWNER_ID"]
DATABASE_URL = config["DATABASE_URL"]
SUDO_USERS = config["SUDO_USERS"]

async def start(update: Update, context: CallbackContext):
    keyboard = [[InlineKeyboardButton("Settings", callback_data="settings")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Welcome to TeraBox Downloader Bot!", reply_markup=reply_markup)

def main():
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))

    # Start polling mode
    app.run_polling()

if __name__ == '__main__':
    main()
