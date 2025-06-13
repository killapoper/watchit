import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

@dp.message(F.text == "/start")
async def start(message: Message, state: FSMContext):
    kb = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="/watch")]
    ], resize_keyboard=True)
    await message.answer("Привет! Добро пожаловать в WatchIT 🎬", reply_markup=kb)

@dp.message(F.text == "/watch")
async def watch(message: Message, state: FSMContext):
    await message.answer("Открывай WatchIT 👉 https://352d-57-129-37-188.ngrok-free.app или https://352d-57-129-37-188.ngrok-free.app")

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())