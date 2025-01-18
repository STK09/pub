from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from utils.helpers import is_admin, send_broadcast_message

async def broadcast_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if not is_admin(user_id):
        await update.message.reply_text("❌ You do not have admin permissions to use this command.")
        return

    if not context.args:
        await update.message.reply_text("⚠️ Use `/broadcast <message>` to send a broadcast.")
        return

    message = " ".join(context.args)
    if "http" in message:  # A very simple check to differentiate normal text vs link/image/video
        keyboard = [
            [InlineKeyboardButton("Click Me", url=message)]  # Add an inline button for links
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        message = "Broadcasting with Inline Button! 👇"
    else:
        reply_markup = None

    for user_id in get_all_users():
        await send_broadcast_message(update.bot, user_id, message, reply_markup)
    await update.message.reply_text("✅ Broadcast message sent to all users!")
