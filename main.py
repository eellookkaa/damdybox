import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message

# Get bot token from Railway environment variables
TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("BOT_TOKEN is not set in environment variables")

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Example handler
@dp.message()
async def echo_handler(message: Message):
    await message.answer(f"Hello 👋, you wrote: {message.text}")

async def main():
    # Start bot
    print("🤖 Bot is running...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
