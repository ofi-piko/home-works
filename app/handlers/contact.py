from aiogram.filters import Command
from aiogram import Router, F
from aiogram.types import Message

from app.keyboards.reply import contact_keyboard

router = Router()


@router.message(Command("contact"))
async def contact_command_handler(message: Message):
    await message.answer(
        "Введите свой контакт",
        reply_markup=contact_keyboard()
    )


@router.message(F.contact)
async def get_contact(message: Message):
    phone_number = message.contact.phone_number
    first_name = message.contact.first_name

    await message.answer(
        f"Спасибо, {first_name}! Ваш номер: {phone_number}"
    )