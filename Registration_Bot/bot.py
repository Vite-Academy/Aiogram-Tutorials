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


conn = sqlite3.connect('db.sqlite3', check_same_thread=False)
cursor = conn.cursor()

conn.execute('''
        CREATE TABLE IF NOT EXISTS USERS (
            ID INTEGER NOT NULL PRIMARY KEY,
            FIRST_NAME  TEXT NOT NULL,
            USERNAME TEXT NOT NULL
        );
    ''')
    

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(msg: types.Message):
    await msg.answer('Hi')

    id = msg.from_user.id
    first_name = msg.from_user.first_name
    username = msg.from_user.username
    
    cursor.execute(f'''
                   INSERT INTO USERS (ID, FIRST_NAME, USERNAME) 
                   VALUES ('{id}', '{first_name}', '{username}');
        ''')
    conn.commit()

	
    
# @dp.message_handler()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
