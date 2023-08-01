import sqlite3
import os
from dotenv import load_dotenv
import logging
from aiogram import Bot, Dispatcher, executor, types

load_dotenv()
TOKEN = os.getenv("API_TOKEN")

logging.basicConfig(level=logging.INFO)

bot = Bot(token = TOKEN)
dp = Dispatcher(bot)


# conn = sqlite3.connect('db.sqlite3', check_same_thread=False)
# cursor = conn.cursor()

# conn.execute('''
# CREATE USERS contact(
#          ENG TEXT NOT NULL,
#          RU  TEXT NOT NULL,
#          UZ  TEXT NOT NULL
#         );
#          ''')

# def db_table_val(user_id: int, user_name: str, user_surname: str, username: str):
#     cursor.execute('INSERT INTO USERS (user_id, user_name, user_surname, username) VALUES (?, ?, ?, ?)',
#                    (user_id, user_name, user_surname, username))
#     conn.commit()
    

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.answer('Hi')

    
    # print(message)
    # print(type(message.text)) # Message text: /start <class 'str'>
    # print(type(message.from_user)) # User data: {"id": 1222915427, "is_bot": false, "first_name": "Shakhzod Tojiyev", "username": "shakhzod_tojiyev", "language_code": "en"} <class 'aiogram.types.user.User'>
    # print(type(message.from_id)) # User ID: 1222915427 <class 'int'>
    # print(type(message.message_id)) # Message ID: 102 <class 'int'>
	
    



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
