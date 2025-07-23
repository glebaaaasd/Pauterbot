import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import WebAppInfo
from aiogram.utils import executor

API_TOKEN = os.getenv("BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    web_app = WebAppInfo(url="https://example.com")  # Заменить на реальную ссылку
    keyboard.add(types.KeyboardButton(text="Открыть магазин 🎁", web_app=web_app))
    await message.answer("Добро пожаловать в магазин подарков!", reply_markup=keyboard)

async def start_bot():
    await dp.start_polling()