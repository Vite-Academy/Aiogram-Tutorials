import os
from dotenv import load_dotenv
import logging
from aiogram import Bot, Dispatcher, executor, types
import wikipedia

load_dotenv()
TOKEN = os.getenv("API_TOKEN")

logging.basicConfig(level=logging.INFO)

bot = Bot(token = TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!")


@dp.message_handler()
async def sendWiki(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer("Not found. 😔")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)