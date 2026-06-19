from aiogram import Router, F
from aiogram.filters.callback_data import CallbackData
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery
import logging

from app.keyboards.inline import date_keyboard, time_keyboard
from app.keyboards.reply import masters_keyboard, service_keyboard
from app.utils.logger_config import setup_logger

setup_logger()
logger = logging.getLogger(__name__)

router = Router()

class Form(StatesGroup):
    master = State()
    service = State()
    date = State()
    time = State()

MASTERS = [
    'азиз',
    'андрей',
    'олег'
]

SERVICES = [
    'короткая стрижка',
    'стильная стрижка',
    'стрижка бороды'
]

@router.message(F.text == "✂️ Записаться")
async def book_handler(message: Message, state: FSMContext):
    await state.set_state(Form.master)
    await message.answer(
        text="Выберите мастера:",
        reply_markup=masters_keyboard(MASTERS)
    )

@router.message(
    Form.master,
    F.text.casefold().in_(MASTERS)
)
async def process_master(message: Message, state: FSMContext):
    await state.update_data(master=message.text)
    await state.set_state(Form.service)
    await message.answer(
        text="Напишите название сервиса:",
        reply_markup=service_keyboard(SERVICES)
    )

@router.message(
    Form.service,
    F.text.casefold().in_(SERVICES)
)
async def process_service(message: Message, state: FSMContext):
    await state.update_data(service=message.text)
    await state.set_state(Form.date)
    data = await state.get_data()
    await message.answer(
        text=f'Вы выбрали:\nМастер: {data["master"]}\nУслуга: {data["service"]}'
    )
    await message.answer(
        text=f'Выберите дату:',
        reply_markup=date_keyboard()
    )

@router.callback_query(
    Form.date,
    F.data.startswith("date:")
)
async def process_date(callback: CallbackQuery, state: FSMContext):
    selected_date = callback.data.split(":")[1]

    await state.update_data(date=selected_date)
    await state.set_state(Form.time)
    await callback.answer("Вы выбрали дату")

    await callback.message.edit_text(
        text=f"Вы выбрали дату {selected_date}\n\nТеперь выберите время:",
        reply_markup=time_keyboard()
    )


@router.callback_query(
    Form.time,
    F.data.startswith("time:")
)
async def process_time(callback: CallbackQuery, state: FSMContext):
    selected_time = callback.data.removeprefix("time:")
    await state.update_data(time=selected_time)
    data = await state.get_data()

    await callback.answer("Вы выбрали время")

    await callback.message.edit_text(
        text=f"Вы выбрали дату {data['date']}\nВыбрали время: {data['time']}"
    )

    await state.clear()










