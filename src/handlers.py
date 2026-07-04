from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram import F


from src.keyboards import keyboard_main, inline





router = Router()



@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        f"Привет {message.from_user.first_name}! Я бот.",
        reply_markup=keyboard_main
        )
    print(f"Пользователь {message.from_user.first_name} отправил {message} в {message.date}")


@router.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer(
        "Я могу помочь вам с различными задачами.\n\n"
        "Вот список доступных команд:\n"
        "/start - начать взаимодействие с ботом\n"
        "/help - получить справку о боте\n"
        "/about - узнать информацию о боте",
        reply_markup=inline
    )


@router.callback_query(F.data == "show_start")
async def show_start(callback: CallbackQuery):
    await callback.answer('Вы готовы инвалиды?', show_alert=True)
    await callback.message.answer("Начинаем наше кулинарное шоу!")

@router.message(Command("about"))
async def cmd_about(message: Message):
    await message.answer(
        "🤖 Я Telegram-бот.\n\n"
        "Мои возможности:\n"
        "• отвечать на команды\n"
        "• помогать пользователям\n"
        "• выполнять различные задачи\n\n"
        "Версия бота: 1.0"
    )


@router.message(F.text.lower() == "пока")
async def say_goodbaye(message: Message):
    await message.answer("Пока! До скорой встречи!")



@router.message(F.text == "Корзина")
async def get_group(message: Message):
    await message.answer("Привет, твоя корзина пуста! Добавь что-нибудь в нее.")
    


@router.message()
async def echo(message: Message):
    await message.answer(message.text)