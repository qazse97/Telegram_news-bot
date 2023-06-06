from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Останні новини")
        ],
        [
            KeyboardButton(text="Новини за категорією")
        ],
        [
            KeyboardButton(text="Новини за ключовим словом")
        ],
        [
            KeyboardButton(text="Підписка на категорію")
        ],
        [
            KeyboardButton(text="Збережені новини")
        ],
    ],
    resize_keyboard=True
)

categories_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Спорт", callback_data="category_bombardyr_ua")
        ],
        [
            InlineKeyboardButton(text="Економіка", callback_data="category_OstanniyCapitalist")
        ],
        [
            InlineKeyboardButton(text="Політика", callback_data="category_resurgammmm")
        ],
        [
            InlineKeyboardButton(text="Світ", callback_data="category_suspilnenews")
        ],
        [
            InlineKeyboardButton(text="Технології", callback_data="category_blognot")
        ],
        [
            InlineKeyboardButton(text="Україна", callback_data="category_V_Zelenskiy_official")
        ],
        [
            InlineKeyboardButton(text="Війна", callback_data="category_voynareal")
        ],
        [
            InlineKeyboardButton(text="Кіно", callback_data="category_zagin_kinomaniv")
        ],
    ]
)


subscription_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Спорт", callback_data="subscription_bombardyr_ua")
        ],
        [
            InlineKeyboardButton(text="Економіка", callback_data="subscription_OstanniyCapitalist")
        ],
        [
            InlineKeyboardButton(text="Політика", callback_data="subscription_resurgammmm")
        ],
        [
            InlineKeyboardButton(text="Світ", callback_data="subscription_suspilnenews")
        ],
        [
            InlineKeyboardButton(text="Технології", callback_data="subscription_blognot")
        ],
        [
            InlineKeyboardButton(text="Україна", callback_data="subscription_V_Zelenskiy_official")
        ],
        [
            InlineKeyboardButton(text="Війна", callback_data="subscription_voynareal")
        ],
        [
            InlineKeyboardButton(text="Кіно", callback_data="subscription_zagin_kinomaniv")
        ]
    ]
)


