import random
import re
import sqlite3

from pyrogram import Client

from config import channels_username
from keyboards import menu_keyboard, categories_keyboard, subscription_keyboard
from bot import dp

from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

app = Client("my_account")


@dp.message_handler(state="*", commands=["start"])
async def cmd_start(message: Message):
    await message.answer("Головне меню", reply_markup=menu_keyboard)


@dp.message_handler(state="*", text="Останні новини")
async def last_news(message: Message):
    random_channels = random.sample(channels_username, 5)
    for channel_username in random_channels:
        last_post = ""
        async for post in app.get_chat_history(chat_id=channel_username):
            last_post = post
            if last_post.caption is not None or last_post.text is not None:
                break
            else:
                continue
        text = last_post.text if last_post.caption is None else last_post.caption
        text = f"{text[:100]}...\n\n" \
               f"{last_post.link}" if len(text) > 30 else f"{text}\n\n" \
                                                          f"{last_post.link}"

        saved_keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text="Зберегти", callback_data="save_news")
                ]
            ]
        )
        await message.answer(text, disable_web_page_preview=True, reply_markup=saved_keyboard)


@dp.message_handler(state="*", text="Новини за категорією")
async def last_news(message: Message):
    await message.answer("Обери категорію", reply_markup=categories_keyboard)


@dp.callback_query_handler(state="*", text_startswith="category")
async def category_last_news(call: CallbackQuery):
    await call.message.delete()
    channel_username = call.data[9:]
    index = 5
    posts = []
    async for post in app.get_chat_history(chat_id=channel_username):
        last_post = post
        if last_post.caption is not None or last_post.text is not None:
            if index == 0:
                break
            index -= 1
            posts.append(post)
        else:
            continue
    for post in posts:
        text = post.text if post.caption is None else post.caption
        text = f"{text[:100]}...\n\n" \
               f"{post.link}" if len(text) > 30 else f"{text}\n\n" \
                                                     f"{post.link}"
        saved_keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text="Зберегти", callback_data="save_news")
                ]
            ]
        )
        await call.message.answer(text, disable_web_page_preview=True, reply_markup=saved_keyboard)


@dp.message_handler(state="*", text="Новини за ключовим словом")
async def key_last_news(message: Message):
    await message.answer("Введи ключове слово")


@dp.message_handler(state="*", text="Підписка на категорію")
async def subscription_categories(message: Message):
    await message.answer("Обери категорії, на які хочеш підписатися", reply_markup=subscription_keyboard)


@dp.callback_query_handler(state="*", text_startswith="subscription")
async def subscription_categories(call: CallbackQuery):
    db = sqlite3.connect("database.db")
    cursor = db.cursor()
    channel_username = call.data[13:]
    new_subscription_keyboard = InlineKeyboardMarkup()
    for button in call.message.reply_markup.inline_keyboard:
        button_text = button[0].text
        if button[0].callback_data == call.data:
            if "✅" in button_text:
                button_text = button_text[:-2]
                cursor.execute("UPDATE subscription SET subscription_status = ? WHERE channel_username = ?",
                               (0, channel_username))
                db.commit()
            else:
                button_text = f"{button_text} ✅"
                cursor.execute("UPDATE subscription SET subscription_status = ? WHERE channel_username = ?",
                               (1, channel_username))
                db.commit()

        button = InlineKeyboardButton(text=button_text, callback_data=button[0].callback_data)
        new_subscription_keyboard.add(button)

    db.close()
    await call.message.edit_reply_markup(reply_markup=new_subscription_keyboard)


@dp.message_handler(state="*", text="Збережені новини")
async def answer_saved_news(message: Message):
    db = sqlite3.connect("database.db")
    cursor = db.cursor()
    cursor.execute("SELECT news_text FROM saved_news")
    news = cursor.fetchall()
    db.close()
    for text in news:
        await message.answer(text[0], disable_web_page_preview=True)


@dp.callback_query_handler(state="*", text="save_news")
async def save_news(call: CallbackQuery):
    news_text = call.message.text
    db = sqlite3.connect("database.db")
    cursor = db.cursor()

    cursor.execute("INSERT INTO saved_news VALUES (?)", (news_text,))
    db.commit()
    db.close()
    await call.message.edit_reply_markup(reply_markup=None)


@dp.message_handler(state="*")
async def key_last_news(message: Message):
    key_word = message.text
    found_key = False
    for channel_username in channels_username:
        index = 0
        async for post in app.get_chat_history(chat_id=channel_username):
            last_post = post
            if last_post.caption is not None or last_post.text is not None:
                text = last_post.text if last_post.caption is None else last_post.caption
                find_key = re.search(key_word, text, re.IGNORECASE)
                if find_key:
                    found_key = True
                    text = f"{text[:100]}...\n\n" \
                           f"{last_post.link}" if len(text) > 30 else f"{text}\n\n" \
                                                                      f"{last_post.link}"
                    saved_keyboard = InlineKeyboardMarkup(
                        inline_keyboard=[
                            [
                                InlineKeyboardButton(text="Зберегти", callback_data="save_news")
                            ]
                        ]
                    )
                    await message.answer(text, disable_web_page_preview=True, reply_markup=saved_keyboard)
                if index > 50:
                    break
            else:
                continue
            index += 1
    if not found_key:
        await message.answer("Ключове слово не знайдено!")









































