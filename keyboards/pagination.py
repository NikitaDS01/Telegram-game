from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton



class ReportPagination(CallbackData, prefix = "report"):
    action: str
    page: int

def report_pagination(page: int = 0):
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="◀️", callback_data=ReportPagination(action="prev", page = page).pack()),
        InlineKeyboardButton(text="▶️", callback_data=ReportPagination(action="next", page = page).pack()),
        width = 2
    )
    builder.row(
        InlineKeyboardButton(text="Вернуться", callback_data="return_admin_panel_1"),
        width=1
    )
    return builder.as_markup()