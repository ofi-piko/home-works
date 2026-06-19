from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from datetime import datetime, timedelta

TIMES = [f"{i}:00" for i in range(10, 24)]

def date_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    for i in range(7):
        date = datetime.now() + timedelta(days=i)

        builder.button(
            text=date.strftime("%d.%m"),
            callback_data=f"date:{date.strftime('%Y-%m-%d')}"
        )

    return builder.as_markup(resize_keyboard=True, one_time_keyboard=True)

def time_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    for time in TIMES:
        builder.button(
            text=time,
            callback_data=f"time:{time}"
        )

    builder.adjust(4)

    return builder.as_markup(resize_keyboard=True, one_time_keyboard=True)
    


















