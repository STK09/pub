from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from config import BOT_TOKEN
from commands import start, link, batch, broadcast

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Command Handlers
    app.add_handler(CommandHandler("start", start.start_command))
    app.add_handler(CommandHandler("link", link.link_command))
    app.add_handler(CommandHandler("batch", batch.batch_command))
    app.add_handler(CommandHandler("broadcast", broadcast.broadcast_command, filters=filters.User(username="YourAdminUsername")))

    # Run the bot
    print("🤖 Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
