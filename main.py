import asyncio
import threading
import os
from server import app
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton
from config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(F.text == "/start")
async def cmd_start(message: types.Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📺 Открыть каталог", web_app=WebAppInfo(url="https://watchit-3b7r.onrender.com"))]
    ])
    await message.answer("Добро пожаловать в FreeCinema!", reply_markup=keyboard)

def run_web():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    threading.Thread(target=run_web, daemon=True).start()
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
