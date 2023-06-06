import logging

from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler

from config import TOKEN

bot = Bot(TOKEN, parse_mode="HTML")
dp = Dispatcher(bot, storage=MemoryStorage())
logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    from subscription import get_channel_message
    from handlers import dp, app
    from admin_panel import dp

    app.start()
    app.add_handler(MessageHandler(get_channel_message, filters=filters.channel))
    executor.start_polling(dp)
    app.stop()
