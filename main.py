import asyncio
import logging


from aiogram import Bot, Dispatcher
from src.handlers import router
from config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()       #обработчик входящих обновлений


async def main():
    logging.basicConfig(level=logging.INFO)
    dp.include_router(router)
    await dp.start_polling(bot)     #отправляет запрос на тг-сервер


if __name__ == "__main__":
   try:
        asyncio.run(main())
   except (KeyboardInterrupt, SystemExit):
        print("Бот остановлен!")
       

