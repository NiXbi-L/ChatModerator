import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from config import BotSetings
from Handlers import router  # Импортируем роутер из handlers.py

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=BotSetings.token)
dp = Dispatcher()

# Включаем роутер
dp.include_router(router)

async def main():
    # Удаляем вебхук и запускаем поллинг
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())