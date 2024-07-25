import logging
import asyncio

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command

from database.requests import get
from keyboards import reply, pagination
from motor.core import AgnosticDatabase as MDB
from database.models.report import Report

router = Router()

__str_panel_admin = "👑 Панель администратора\n"
__str_panel_report = "📰 Панель для работы с репортами"
__str_report = "Создан:\n{0}\nСтатус: {1}\nСообщение: {2}\nСтраница {3}/{4}"
__str_count_report = "Количество баг-репорт: {0}"

### Команда админ-панели
@router.callback_query(F.data == "return_admin_panel_1")
@router.message(Command("admin"))
async def fill_report(message: Message | CallbackQuery):
    if(isinstance(message, Message)):
        await message.answer(
            __str_panel_admin,
            reply_markup= reply.get_admin_panel()
        )
    else:
        await message.message.edit_text(
            __str_panel_admin,
            reply_markup= reply.get_admin_panel()
    )

### Команда для работы с репортами
@router.callback_query(F.data == "panel_report_1")
async def print_panel_report(query: CallbackQuery, db: MDB):
    await query.message.edit_text(
        __str_panel_report,
        reply_markup= reply.get_report_panel()
    )

@router.callback_query(pagination.ReportPagination.filter(F.action =="prev"))
async def prev_report_pagination(query: CallbackQuery, db: MDB, callback_data: pagination.ReportPagination):
    page = int(callback_data.page) - 1
    count = await get.count_report(db = db)
    if(page < 0): 
        await query.answer()
        return

    cursor = await get.many_report(db = db,
                                       skip = page,
                                       limit=1)
    json = await cursor.next()
    report = Report.convert(json)

    await query.message.edit_text(
        str.format(__str_report,
                   report.create_report,
                   report.status, 
                   report.message,
                   page + 1, count),
        reply_markup= pagination.report_pagination(page = page)
    )

@router.callback_query(pagination.ReportPagination.filter(F.action =="next"))
async def next_report_pagination(query: CallbackQuery, db: MDB, callback_data: pagination.ReportPagination):
    page = int(callback_data.page) + 1
    count = await get.count_report(db = db)
    if(page >= count): 
        await query.answer()
        return

    cursor = await get.many_report(db = db,
                                       skip = page,
                                       limit=1)
    json = await cursor.next()
    report = Report.convert(json)

    await query.message.edit_text(
        str.format(__str_report,
                   report.create_report,
                   report.status, 
                   report.message,
                   page + 1, count),
        reply_markup= pagination.report_pagination(page = page)
    )

### Команда для обработки репортов
@router.callback_query(F.data == "read_report_1")
async def read_report(query: CallbackQuery, db: MDB):
    count = await get.count_report(db = db)
    if(count == 0):
        query.bot.answer_callback_query(query.id,
                                        text="В репортах пусто",
                                        show_alert=True)
    cursor = await get.many_report(db = db,
                                       skip = 0,
                                       limit=1)
    json = await cursor.next()
    report = Report.convert(json)
    await query.message.edit_text(
        str.format(__str_report,
                   report.create_report,
                   report.status, 
                   report.message,
                   0, count),
        reply_markup= pagination.report_pagination(page = 0)
    )
    
### Команда для вывода количество репортов
@router.callback_query(F.data == "count_report_1")
async def count_print_report(query: CallbackQuery, db: MDB):
    count = await get.count_report(db = db)
    await query.message.edit_text(
        str.format(__str_count_report, count),
        reply_markup= reply.get_return_admin_panel()
    )