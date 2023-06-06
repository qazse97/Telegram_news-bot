from aiogram.dispatcher.filters.state import StatesGroup, State


class Form(StatesGroup):
    place = State()
    height = State()
    weight = State()
    chest = State()
    age = State()
    condition = State()
    budget = State()
    passport = State()
    visa = State()
    media = State()
    verification = State()