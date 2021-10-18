from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(CommandStart(), state="*")
async def bot_start(message: types.Message):
    await message.answer(f"Assalomu Alaykum, {message.from_user.full_name}!\n\nBotdan foydalanish uchun /calendar buyrug'ini tanlang.")
