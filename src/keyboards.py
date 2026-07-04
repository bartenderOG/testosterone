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


def get_start_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Зарегистрироваться")]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )


def get_confirmation_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Подтвердить", callback_data="confirm_reg"),
                InlineKeyboardButton(text="Начать заново", callback_data="restart_reg")
            ]
        ]
    )