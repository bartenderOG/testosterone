
import asyncio
import logging


from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from src.handlers import router
from config import BOT_TOKEN
from db.database import init_db



bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())       #обработчик входящих обновлений


async def main():
    init_db()
    await bot.delete_webhook(drop_pending_updates=True)
    dp.include_router(router)
    await dp.start_polling(bot)     #отправляет запрос на тг-сервер


if __name__ == "__main__":
   logging.basicConfig(level=logging.INFO)
   try:
        asyncio.run(main())
   except (KeyboardInterrupt, SystemExit):
        print("Бот остановлен!")
       

