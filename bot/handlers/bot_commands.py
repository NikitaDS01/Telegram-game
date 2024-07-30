from loguru import logger as log
from datetime import datetime

from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from motor.motor_asyncio import AsyncIOMotorClient

from database.models.report import Report
from database.models.user import User
from database.requests.include import IncludeReport
from bot.utils.states import StateReport


router = Router()

### Команда старта
@router.message(CommandStart())
async def start(message: Message, db: AsyncIOMotorClient):
    #if not(await get.one_user(db = db, filter = {'_id':message.from_user.id}) is None):
        #await message.answer(f"Здарова обратно {message.from_user.first_name}")
        #return
    
    #user = User(
     #       telegram_id = message.from_user.id,
      #      status = 'user',
       #     dialog_name = 'None',
        #    dialog_index = -1,
         #   money = [0, 0],
          #  inventory = list(),
           # properties = list(),
            #abilities = list(),
            #effects = list()
    #)
    # await include.one_user(db = db, user = user)
    log.debug(f"Command start {message.from_user.id}")
    await message.answer(f"Здарова {message.from_user.first_name}")
    

### Репорт сообщения
@router.message(F.text, Command("report"))
async def fill_report(message: Message, state: FSMContext):
    log.debug(f"Command report 1 {message.from_user.id}")
    await state.set_state(StateReport.Message)
    await message.answer("Отправьте баг-репорт в виде сообщения")

@router.message(F.text, StateReport.Message)
async def form_message(message: Message, db: AsyncIOMotorClient, state: FSMContext):
    log.debug(f"Command report 2 {message.from_user.id}")
    report = Report(user_id = message.from_user.id,
                    create_report = datetime.now(),
                    message = message.text,
                    status = 0)
    await IncludeReport.one_async(
        db = db.games,
        report = report
    )
    await message.answer("Спасибо за баг-репорт")
    await state.clear()

### Обработка всех сообщений
@router.message(F.text)
async def message_processing(message: Message, db: AsyncIOMotorClient):
    log.debug(f"Command null {message.from_user.id}")
    #user = await get.one_user(db = db, filter = {'_id':message.from_user.id})
    #if user is None:
    #    return