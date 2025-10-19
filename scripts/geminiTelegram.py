import asyncio
import logging
import json

# IMPORTANT : To record your chat history,
# you need to create a file called chats.json (or whatever name you like) 
# and change the 'with open' clause!

from google import genai
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
logging.basicConfig(level=logging.INFO, format="%(message)s")

# create dict
chats = {}

# register the important data
log = logging.info
token_bot = ''
gemini_api_key = ''
client = genai.Client(api_key=gemini_api_key)

dp = Dispatcher()
bot = Bot(token=token_bot)
model = "gemini-2.0-flash"
chat = client.chats.create(model='gemini-2.0-flash')

# bot listening to all requests
async def main():
    await dp.start_polling(bot)
    
# started bot command
@dp.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer('Hey! My name is Laura! You ready learning English?')

# create chat command with history (chats)
@dp.message(Command("create_chat"))
async def create_handler(message: types.Message):
    try:
        with open('chats.json', 'r', encoding='utf-8') as f:
            
            user_id = message.from_user.id

        if user_id in chats:
            await message.reply("you have chat, cannot create new!")
        else:
            
            chats[user_id] = {"history": []}
        
            with open('chats.json', "w", encoding="utf-8") as f:
                json.dump(chats, f, indent=2, ensure_ascii=False)
            
            await message.reply("succesfully chat created!")
            
    except Exception as e:
        log(f'create error - {e}')

# here we speaking to bot, and he responds to any of our commands
@dp.message()
async def gemini_handler(message: types.Message):
    
    try:
        with open('chats.json', 'r', encoding='utf-8') as f:
            user_id = message.from_user.id

        if user_id not in chats:
            await message.reply("you mustn create chat: /create_chat")
            return

        user_message = message.text
        requests = chat.send_message(user_message)
        rspc = requests.text
    
        chats[user_id]["history"].append({"user": user_message, "bot": rspc})
    
        with open('chats.json', "w", encoding="utf-8") as f:
            json.dump(chats, f, indent=2, ensure_ascii=False)

        await message.reply(rspc)
        
    except Exception as e:
        log(f'gemini error - {e}')
            
if __name__ == "__main__":
    asyncio.run(main())
