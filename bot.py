import os
import urllib.parse
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import CommandStart
from aiogram import Router
from aiogram.client.default import DefaultBotProperties
from parser import search_baskino
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
RENDER_URL = os.getenv("RENDER_URL")

bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp = Dispatcher(storage=MemoryStorage())
router = Router()

@router.message(CommandStart())
async def start_cmd(message: types.Message):
    kb = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(text="🎬 Открыть каталог", url=RENDER_URL)
    ]])
    await message.answer("Привет! Это <b>Watch It</b> — твой кинотеатр в Telegram.", reply_markup=kb)

@router.message()
async def handle_search(message: types.Message):
    query = message.text.strip()
    results = search_baskino(query)
    if not results:
        return await message.answer("Ничего не найдено по запросу.")
    for m in results:
        kb = InlineKeyboardMarkup(inline_keyboard=[[
            InlineKeyboardButton(
                text="▶️ Смотреть",
                url=f"{RENDER_URL}/watch?url={urllib.parse.quote(m['url'], safe='')}"
            )
        ]])
        await message.answer_photo(photo=m['image'], caption=m['title'], reply_markup=kb)

dp.include_router(router)

if __name__ == "__main__":
    import asyncio
    async def main():
        await dp.start_polling(bot)
    asyncio.run(main())