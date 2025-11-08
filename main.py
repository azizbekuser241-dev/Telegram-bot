
import logging
import wikipedia
import asyncio
from os import getenv
from aiogram import Bot,Dispatcher,types
from aiogram.filters import Command
from aiogram.types import Message
TOKEN = getenv('BOT_TOKEN')

wikipedia.set_lang('uz')
logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher()
@dp.message(Command('start'))
async def send_welcome(message:Message):
    await message.reply("Assalomu alaykum Xush kelibsiz!")
@dp.message()
async def wiki_search(message:Message):
    query = message.text
    try:
        summary = wikipedia.summary(query)
        await message.reply(summary)
    except wikipedia.exeptions.DisabiguationError as e:
        await message.reply("iltimos aniqroq sorov yuboring")
    except Exception as e:
        await message.reply("Xatolik yuz berdi.")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())