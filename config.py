from decouple import config

BOT_TOKEN = config("BOT_TOKEN")
import os
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage


TOKEN = os.getenv("BOT_TOKEN","8817249653:AAENiV742M5MveZ-4nuaElc0-noObDcoRNE" )

bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)


users_data = {}