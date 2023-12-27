import os
from dotenv import load_dotenv
import logging
from aiogram import Bot, Dispatcher, executor, types

load_dotenv()
TOKEN = os.getenv("API_TOKEN")

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token = TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)
    # print(message)
    # print(type(message.text)) # Message text: /start <class 'str'>
    # print(type(message.from_user)) # User data: {"id": 1222915427, "is_bot": false, "first_name": "Shakhzod Tojiyev", "username": "shakhzod_tojiyev", "language_code": "en"} <class 'aiogram.types.user.User'>
    # print(type(message.from_id)) # User ID: 1222915427 <class 'int'>
    # print(type(message.message_id)) # Message ID: 102 <class 'int'>


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)