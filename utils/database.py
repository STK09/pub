from pymongo import MongoClient
from config import MONGO_URI, DATABASE_CHANNEL, BOT_USERNAME

client = MongoClient(MONGO_URI)
db = client["telegram_file_bot"]

def save_file(message_id):
    db.files.insert_one({"message_id": message_id})
    return f"https://t.me/{BOT_USERNAME}?start=file-{message_id}"

def save_batch(bot, chat_id, start_id, end_id):
    for msg_id in range(start_id, end_id + 1):
        bot.forward_message(chat_id=DATABASE_CHANNEL, from_chat_id=chat_id, message_id=msg_id)
        db.files.insert_one({"message_id": msg_id})

def get_all_users():
    return [user["user_id"] for user in db.users.find()]
