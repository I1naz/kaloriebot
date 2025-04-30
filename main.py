import csv
import locale
import sqlite3
import logging
import asyncio

from os import getenv
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, BufferedInputFile
from dotenv import load_dotenv
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiohttp import web

  # замените на ваш URL вебхука

logging.basicConfig(level=logging.INFO)

load_dotenv()

bot = Bot(token=getenv('API_TOKEN'))
dp = Dispatcher()

PORT = int(getenv('PORT'))

#locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')
# locale.setlocale(locale.LC_TIME, 'Russian')



def select_db(id):
    conn = sqlite3.connect('simple.db')
    cursor = conn.cursor()

    # Выборка данных
    cursor.execute(f"SELECT * FROM cities where id == {id}")
    res = cursor.fetchone()
    cursor.close()
    conn.close()
    if res:
        return res
    else:
        return None


def update_city(id, msg):
    conn = sqlite3.connect('simple.db')
    cursor = conn.cursor()

    # Вставка данных
    cursor.execute("UPDATE cities set city = ? where id = ?", (msg, id))
    conn.commit()
    cursor.close()
    conn.close()




def get_start_reply_keyboard():
    keyboard = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="Татарча")]
    ], resize_keyboard=True)
    return keyboard

def get_russian_reply_keyboard():
    keyboard = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="")],
        [KeyboardButton(text="")],
        [KeyboardButton(text="")],
        [KeyboardButton(text="")],
        [KeyboardButton(text="")]

    ], resize_keyboard=True)
    return keyboard

def get_tatar_reply_keyboard():
    keyboard = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="")]
    ], resize_keyboard=True)
    return keyboard


@dp.message(Command("start"))
async def start_command(message: types.Message):
    await message.answer(f'Hello, {message.from_user.first_name}')

@dp.message()
async def echo_message(message: types.Message):
    await message.answer(message.text)


def main():
    app = web.Application()

    # Настройка обработчика запросов вебхука от aiogram (ВАЖНО!)
    webhook_requests_handler = SimpleRequestHandler(dispatcher=dp, bot=bot)

    # Настраиваем приложение aiohttp с использованием aiogram
    webhook_requests_handler.register(app, path="/")
    web.run_app(app, host="0.0.0.0", port=PORT)

if __name__ == "__main__":
    main()

# if __name__ == '__main__':
#     main()
# async def main():
#     await dp.start_polling(bot)
#
# if __name__ == "__main__":
#     asyncio.run(main())


