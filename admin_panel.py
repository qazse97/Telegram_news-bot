from asyncio import sleep

from bot import dp
from config import admin_id

from aiogram.types import Message


@dp.message_handler(state="*", chat_id=admin_id, commands=["send_text"])
async def get_word(message: Message):
    await message.answer("Привет, админ")