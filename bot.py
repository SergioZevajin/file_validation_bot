from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import TOKEN
from handlers import register_handlers
from logger import logger

bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

register_handlers(dp)

if __name__ == "__main__":
    from aiogram import executor    # Избежать циклического импорта;Сделать загрузку бота более оптимизированной; Запустить бота только тогда, когда это нужно
    logger.info("Бот запущен")
    executor.start_polling(dp, skip_updates=True)
