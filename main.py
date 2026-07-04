import asyncio
import logging


from aiogram import Bot, Dispatcher
from src.handlers import router
from config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()       #обработчик входящих обновлений


async def main():
    dp.include_router(router)
    await dp.start_polling(bot)     #отправляет запрос на тг-сервер


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)     #для логирования
    asyncio.run(main())     #для запуска функции

