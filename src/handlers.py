from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from src.keyboards import keyboard_main, inline

from config import users_data
from src.keyboards import get_start_keyboard, get_confirmation_keyboard



router = Router()


class RegistrationStates(StatesGroup):
    waiting_for_name = State()
    waiting_for_age = State()
    waiting_for_confirmation = State()


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
    

@router.message(Command("profile"))
async def cmd_profile(message: Message):
    user_id = message.from_user.id
    if user_id in users_data:
        data = users_data[user_id]
        await message.answer(f"Ваши данные:\nИмя — {data['name']}\nВозраст — {data['age']}")
    else:
        await message.answer("Вы не зарегистрированы. Напишите /start, чтобы пройти регистрацию.")

 
@router.message(F.text == "Зарегистрироваться")
async def start_registration(message: Message, state: FSMContext):
    await message.answer("Шаг 1: Введите ваше имя:")
    await state.set_state(RegistrationStates.waiting_for_name)


@router.message(RegistrationStates.waiting_for_name)
async def process_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Шаг 2: Введите ваш возраст (только число):")
    await state.set_state(RegistrationStates.waiting_for_age)


@router.message(RegistrationStates.waiting_for_age)
async def process_age(message: Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Это не число! Пожалуйста, введите возраст цифрами:")
        return
        
    await state.update_data(age=int(message.text))
    user_data = await state.get_data()
    
    await message.answer(
        f"Ваши данные: Имя — {user_data['name']}, Возраст — {user_data['age']}",
        reply_markup=get_confirmation_keyboard()
    )
    await state.set_state(RegistrationStates.waiting_for_confirmation)


@router.callback_query(RegistrationStates.waiting_for_confirmation, F.data == "confirm_reg")
async def confirm_registration(callback: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    user_id = callback.from_user.id
    
    
    users_data[user_id] = {
        "name": user_data["name"],
        "age": user_data["age"]
    }
    
    await callback.answer("Успешно!")  # Обязательный callback.answer()
    await callback.message.edit_text("Регистрация завершена! 🎉")
    await state.clear() 


@router.callback_query(RegistrationStates.waiting_for_confirmation, F.data == "restart_reg")
async def restart_registration(callback: CallbackQuery, state: FSMContext):
    await callback.answer("Сброс параметров")
    await callback.message.answer("Начнем заново.\nШаг 1: Введите ваше имя:")
    await state.set_state(RegistrationStates.waiting_for_name)