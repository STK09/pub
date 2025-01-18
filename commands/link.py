from telegram import Update
from telegram.ext import ContextTypes
from utils.database import save_file
from config import DATABASE_CHANNEL

async def link_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message.reply_to_message:
        await update.message.reply_text("⚠️ Reply to a file or message with /link to generate a link.")
        return

    file = update.message.reply_to_message
    file_id = file.document.file_id if file.document else file.photo[-1].file_id if file.photo else None
    if not file_id:
        await update.message.reply_text("⚠️ This message cannot be linked.")
        return

    # Forward the file to the database channel
    forwarded_message = await context.bot.forward_message(chat_id=DATABASE_CHANNEL, from_chat_id=update.effective_chat.id, message_id=file.message_id)

    # Save the file info in the database
    file_link = save_file(forwarded_message.message_id)
    await update.message.reply_text(f"✅ File stored successfully!\n🔗 Link: {file_link}")
