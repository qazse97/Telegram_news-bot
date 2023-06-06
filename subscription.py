import sqlite3

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def get_channel_message(client, message):
    db = sqlite3.connect("database.db")
    cursor = db.cursor()
    channel_username = message.chat.username
    cursor.execute("SELECT subscription_status FROM subscription WHERE channel_username = ?", (channel_username,))
    subscription_status = cursor.fetchone()
    if subscription_status is not None:
        if subscription_status[0] == 1:
            text = message.text if message.caption is None else message.caption
            text = f"{text[:100]}...\n\n" \
                   f"{message.link}" if len(text) > 30 else f"{text}\n\n" \
                                                            f"{message.link}"
            saved_keyboard = InlineKeyboardMarkup(
                inline_keyboard=[
                    [
                        InlineKeyboardButton(text="Зберегти", callback_data="save_news")
                    ]
                ]
            )
            await message.answer(text, disable_web_page_preview=True, reply_markup=saved_keyboard)

