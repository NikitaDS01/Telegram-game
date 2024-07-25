import logging
from datetime import datetime

from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext

from database.models.report import Report
from database.models.user import User
from database.requests import include, get

from motor.core import AgnosticDatabase as MDB
from utils.states import StateReport

router = Router()

### Команда старта
@router.message(CommandStart())
async def start(message: Message, db: MDB):
    if not(await get.one_user(db = db, filter = {'_id':message.from_user.id}) is None):
        await message.answer(f"Здарова обратно {message.from_user.first_name}")
        return
    
    user = User(
            telegram_id = message.from_user.id,
            status = 'user',
            dialog_name = 'None',
            dialog_index = -1,
            money = [0, 0],
            inventory = list(),
            properties = list(),
            abilities = list(),
            effects = list()
    )
    await include.one_user(db = db, user = user)
    await message.answer(f"Здарова {message.from_user.first_name}")

### Обработка всех сообщений
@router.message()
async def message_processing(message: Message, db: MDB):
    user = await get.one_user(db = db, filter = {'_id':message.from_user.id})
    if user is None:
        return
    

### Репорт сообщения
@router.message(Command("report"))
async def fill_report(message: Message, state: FSMContext):
    await state.set_state(StateReport.Message)
    await message.answer("Отправьте баг-репорт в виде сообщения")

@router.message(StateReport.Message)
async def form_message(message: Message, db: MDB, state: FSMContext):
    report = Report(user_id = message.from_user.id,
                           create_report = datetime.now(),
                           message = message.text,
                           status = 'NEW')
    await include.one_report(db = db,
                                     report = report)
    await message.answer("Спасибо за баг-репорт")
    await state.clear()