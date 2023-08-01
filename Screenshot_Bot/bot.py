import os
from PIL import ImageGrab
import secrets
from dotenv import load_dotenv
import logging
from aiogram import Bot, Dispatcher, executor, types

load_dotenv()
TOKEN = os.getenv("API_TOKEN")

logging.basicConfig(level=logging.INFO)

bot = Bot(token = TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!")


@dp.message_handler(commands=['screen'])
async def screenshot(msg: types.Message) -> None:
    img = ImageGrab.grab()
    if not os.path.exists('static'):
        os.mkdir('static')
    os.chdir('static')
    img_name = secrets.token_hex(8) + '.png'
    img.save(img_name, format='PNG')

    with open(img_name, 'rb') as f:
        await msg.answer_photo(photo=f)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)