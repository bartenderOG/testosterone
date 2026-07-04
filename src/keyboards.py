from aiogram.types import (ReplyKeyboardMarkup, 
                            KeyboardButton,
                            InlineKeyboardMarkup,
                            InlineKeyboardButton
                            )


keyboard_main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Корзина")],
    [KeyboardButton(text="Профиль"), KeyboardButton(text="Каталог")],
], resize_keyboard=True,  input_field_placeholder="Выбери один пункт")


inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Перейти на сайт", url="https://geeks.kg")],
    [InlineKeyboardButton(text="Начинаем наше кулинарное шоу", callback_data="show_start")]
])