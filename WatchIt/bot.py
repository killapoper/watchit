from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils import executor
import os
from parser import search_baskino
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(msg: types.Message):
    await msg.answer("👋 Привет! Напиши название фильма.")

@dp.message_handler()
async def search(msg: types.Message):
    query = msg.text.strip()
    movies = search_baskino(query)
    if not movies:
        await msg.answer("❌ Ничего не найдено.")
        return

    for movie in movies[:5]:
        btn = InlineKeyboardMarkup().add(
            InlineKeyboardButton("Смотреть", url=movie['https://watchit-3b7r.onrender.com'])
        )
        await msg.answer_photo(movie['image'], caption=movie['title'], reply_markup=btn)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
