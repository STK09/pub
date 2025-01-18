from telegram import Update
from telegram.ext import ContextTypes

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "ℹ️ **Help Guide**:\n\n"
        "**/start** - Starts the bot and gives you an overview.\n"
        "**/link** - Create a permanent link for a file. Reply to a file and type `/link`.\n"
        "**/batch** - Store multiple files in batch from a channel. Use `/batch start_id end_id`.\n"
        "**/broadcast** - Send a message to all users (admins only).\n\n"
        "If you need any further assistance, feel free to ask! 😊"
    )
