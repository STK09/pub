from telegram import Update
from telegram.ext import ContextTypes
from utils.database import save_batch

async def batch_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args or len(context.args) < 2:
        await update.message.reply_text("⚠️ Use `/batch start_message_id end_message_id` to store files.")
        return

    start_id, end_id = map(int, context.args)
    await save_batch(context.bot, update.effective_chat.id, start_id, end_id)
    await update.message.reply_text("✅ Batch files stored successfully!")
