from config import LOG_CHANNEL

async def log_action(bot, action):
    await bot.send_message(
        chat_id=LOG_CHANNEL,
        text=action
    )

def log_user_start(bot, user_id, username):
    log_action(bot, f"👤 User @{username} ({user_id}) has just started the bot.")

def log_command(bot, user_id, command):
    log_action(bot, f"👤 User {user_id} executed command: /{command}")
