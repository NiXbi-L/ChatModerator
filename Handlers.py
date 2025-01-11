from aiogram import Router, types
from aiogram.filters import Command
from GPTmoderation import chek  # Импортируем функцию chek
import asyncio

# Создаем роутер
router = Router()


# Хендлер для команды /start
@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Привет! Я бот-модератор. Отправь мне сообщение, и я проверю его на нарушения.")


# Хендлер для обработки текстовых сообщений
@router.message()
async def handle_message(message: types.Message):
    result = await asyncio.to_thread(chek, message.text)
    if result[0]:
        await message.delete()