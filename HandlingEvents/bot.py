import asyncio
import logging
import sys
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold

load_dotenv()
TOKEN = os.getenv("API_TOKEN")

logging.basicConfig(level=logging.INFO)

bot = Bot(token = TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!")
    

# @dp.message_handler(content_types='text') # Default str format handler
# async def str_handler(msg: types.Message) -> None:
#     await msg.answer_dice() # Message methods
#     await bot.send_dice(msg.chat.id) # Bot methods
    # await msg.answer(f'{msg.text}, {type(msg.text)}') # Message methods
    # await bot.send_message(msg.from_user.id, text="The End") # Bot methods


@dp.message_handler(content_types='sticker')
async def sticker_handler(msg: types.Message) -> None:
    await msg.answer(type(msg))
    await msg.answer_sticker(sticker=msg.sticker.file_id)

@dp.message_handler(content_types='photo')
async def photo_handler(msg: types.Message) -> None:
    await msg.answer(type(msg))
    # print(msg)


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())