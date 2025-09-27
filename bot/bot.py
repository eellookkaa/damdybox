import os
import asyncio
from aiogram import Bot, Dispatcher, types

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message()
async def echo(msg: types.Message):
    await msg.answer("Привет! Я работаю на Railway 🚀")

async def start_bot():
    await dp.start_polling(bot)
