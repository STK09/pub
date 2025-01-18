from config import ADMIN_IDS

def is_admin(user_id):
    return user_id in ADMIN_IDS

async def send_broadcast_message(bot, user_id, message):
    try:
        await bot.send_message(chat_id=user_id, text=message)
    except Exception as e:
        print(f"Failed to send broadcast message to {user_id}: {e}")
