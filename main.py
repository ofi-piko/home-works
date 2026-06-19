import logging
import asyncio
from os import getenv
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher

from app.utils.logger_config import setup_logger
from app.handlers.start import router as start_router
from app.handlers.custom import router as custom_router
from app.handlers.menu import router as menu_router
from app.handlers.book import router as book_router
from app.handlers.contact import router as contact_router

from app.db.model import start_running

setup_logger()
logger = logging.getLogger(__name__)

load_dotenv()
TOKEN = getenv("BOT_TOKEN")

dp = Dispatcher()

dp.include_router(start_router)
dp.include_router(custom_router)
dp.include_router(menu_router)
dp.include_router(book_router)
dp.include_router(contact_router)


async def main():
    await start_running()

    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())