import asyncio
import logging
import sys
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Filter
from aiogram.types import Message, Chat
from aiogram.utils.markdown import hbold
from aiogram.methods import SendPhoto, GetMe

load_dotenv()
TOKEN = os.getenv("API_TOKEN")

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    # await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")
    # await message.answer_photo(photo='https://images.unsplash.com/photo-1554080353-a576cf803bda?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8cGhvdG98ZW58MHx8MHx8fDA%3D',
    #                            caption='This is amazing!',
    #                            has_spoiler=True)
      await message.send_copy(chat_id=message.chat.id)

# @dp.message()
# async def echo_handler(message: types.Message) -> None:
#     try:
#         await message.send_copy(chat_id=message.chat.id)
#     except TypeError:
#         await message.answer("Nice try!")



async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())