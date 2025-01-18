from telegram import Update
from telegram.ext import ContextTypes
from utils.logging import log_user_start

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    log_user_start(update.bot, user.id, user.username)
    await update.message.reply_text(
        f"👋 Hi {user.first_name}! Welcome to the File Storage Bot.\n\n"
        "Here are the commands you can use:\n"
        "/link - Generate a permanent link for a file.\n"
        "/batch - Batch store files from a channel.\n"
        "/help - Get detailed instructions."
    )
