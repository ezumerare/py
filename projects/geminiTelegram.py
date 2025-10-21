import asyncio
import logging
import aiosqlite

# IMPORTANT : To record your chat history,
# you need to create a file called example data.db (or whatever name you like) 

from google import genai
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
logging.basicConfig(level=logging.INFO, format="%(message)s")


# register the important data
log = logging.info
token_bot = ''
gemini_api_key = ''
client = genai.Client(api_key=gemini_api_key)

log(f'Database is connected!')
log(f'Cursor created!')

dp = Dispatcher()
bot = Bot(token=token_bot)
model = "gemini-2.0-flash"
chat = client.chats.create(model='gemini-2.0-flash')


# save all messages to database
async def save_message(user_id, requests, response):
        connecting = await aiosqlite.connect('data.db')
        cursor = await connecting.cursor() 
        await cursor.execute('INSERT INTO DATA (user, message, response) VALUES (?, ?, ?)', (user_id, requests, response))
        return await cursor.commit()

# bot listening to all requests
async def main():
    await dp.start_polling(bot)

# function
async def require_message_data(user_id):
        connecting = await aiosqlite.connect('data.db')
        cursor = await connecting.cursor() 
        
        await cursor.execute('SELECT * FROM DATA WHERE user = ?', (user_id,))
        return await cursor.fetchone()
        
        
# started bot command
@dp.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer('Hey! My name is Laura! You ready learning English?')
    
# create chat command with history (chats)
@dp.message(Command("create_chat"))
async def create_handler(message: types.Message):
    async with aiosqlite.connect('data.db') as data:
        cursor = await data.cursor() 
        
        user_id = message.from_user.id
    
        await cursor.execute('CREATE TABLE IF NOT EXISTS DATA (user TEXT, requests TEXT, response TEXT)')
    
        
        search = require_message_data(user_id)
        
        try:
            if search is None:
                await cursor.execute('INSERT OR IGNORE INTO DATA (user, requests, response) VALUES (?, ?, ?)', (user_id, 'requests', 'response'))
                await message.reply("succesfully chat created!")
            
                save_message(user_id, 'requests', 'response')
                return
        
            else:
                await message.reply("you have chat, cannot create new!")
                
        except aiosqlite.Error as e:
            log(f'error - {e}')

        
        
# here we speaking to bot, and he responds to any of our commands
@dp.message()
async def gemini_handler(message: types.Message):
        user_id = message.from_user.id
    
        try:
            search = require_message_data(user_id)
        
            if search is None:
                await message.reply('you mustn create chat: /create_chat')
                return
            
            user_message = message.text
            requests = chat.send_message(user_message)
            response = requests.text
            
            save_message(user_id, requests, response)
            
            await message.reply(response)
        
        except aiosqlite.Error as e:
            log(f'error - {e}')
        
if __name__ == "__main__":
    asyncio.run(main())
