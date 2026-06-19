from aiogram import Router, F
from aiogram.types import Message

router = Router()

@router.message(F.text == "📖 Активные записи")
async def active_bookings_handler(message: Message):
    await message.answer(
        text="Ваши Активные записи"
    )

@router.message(F.text == "🎄 Помощь")
async def help_handler(message: Message):
    await message.answer(
        text="Помощь"
    )
