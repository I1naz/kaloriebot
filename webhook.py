import asyncio
import logging
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
import os

load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")
WEBHOOK_HOST = os.getenv("WEBHOOK_URL")  # Укажите свой домен

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Обработчик сообщений
@dp.message()
async def setting_webhook():
    await bot.set_webhook(WEBHOOK_HOST)

async def webhook_info():
    await bot.get_webhook_info()



if __name__ == '__main__':
    asyncio.run(setting_webhook())

