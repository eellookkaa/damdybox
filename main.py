import asyncio
import uvicorn
from backend.main import app
from bot.bot import start_bot

async def start():
    bot_task = asyncio.create_task(start_bot())
    api_task = asyncio.create_task(
        uvicorn.run(app, host="0.0.0.0", port=8000)
    )
    await asyncio.gather(bot_task, api_task)

if __name__ == "__main__":
    asyncio.run(start())
