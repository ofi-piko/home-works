from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def start_menu_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="✂️ Записаться")],
            [KeyboardButton(text="📖 Активные записи")],
            [KeyboardButton(text="🎄 Помощь")]
        ],
        resize_keyboard=True,
        input_field_placeholder="Выберите действие:",
        one_time_keyboard=True
    )


def masters_keyboard(masters: list[str]) -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()

    for master in masters:
        builder.button(
    text=master.capitalize())
    builder.adjust(1)

    return builder.as_markup(resize_keyboard=True, one_time_keyboard=True)

def service_keyboard(services: list[str]) -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()

    for service in services:
        builder.button(text=service.capitalize())

    builder.adjust(1)

    return builder.as_markup(resize_keyboard=True, one_time_keyboard=True)


def contact_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(
                    text="Поделиться контактом",
                    request_contact=True
                )
            ]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )











