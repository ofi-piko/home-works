from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message

from app.keyboards.reply import start_menu_keyboard

router = Router()

@router.message(F.text == "Старт")
@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(
        text="Привет, я бот для бронирования и записей!",
        reply_markup=start_menu_keyboard()
    )