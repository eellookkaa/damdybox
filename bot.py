import logging
from aiogram import Bot, Dispatcher, executor, types

import os
API_TOKEN = os.getenv("BOT_TOKEN")

# Включаем логирование
logging.basicConfig(level=logging.INFO)

# Создаём экземпляры
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


# Приветствие
@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    text = (
        "Привет! Я DámdyBox 🤖\n"
        "Я помогу тебе находить вкусные наборы еды по выгодным ценам 🎁\n\n"
        "👉 Нажми /menu, чтобы посмотреть доступные боксы."
    )
    await message.answer(text)


# Простое меню
@dp.message_handler(commands=["menu"])
async def show_menu(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("🍱 Посмотреть боксы", "ℹ️ О проекте")
    await message.answer("Выбери действие:", reply_markup=keyboard)


# Ответы на кнопки
@dp.message_handler(lambda m: m.text == "🍱 Посмотреть боксы")
async def show_boxes(message: types.Message):
    await message.answer("Сегодня доступны:\n\n1. 🥗 Салаты — 1500₸\n2. 🍕 Пицца — 2000₸\n3. 🍩 Десерты — 1000₸")


@dp.message_handler(lambda m: m.text == "ℹ️ О проекте")
async def about(message: types.Message):
    await message.answer("DámdyBox — сервис, который помогает находить вкусные наборы по суперцене ✨")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
