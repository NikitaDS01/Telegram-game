from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import KeyboardButton
from aiogram.types import ReplyKeyboardRemove

from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup
from aiogram.types import InlineKeyboardButton

rmk = ReplyKeyboardRemove()


admin_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="☕ Искать собеседника")],
        [KeyboardButton(text="🍪 Профиль")]
    ],
    resize_keyboard=True
)

def get_admin_panel() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(text="📕 Панель репортов", callback_data="panel_report_1"),
        InlineKeyboardButton(text="Количество игроков", callback_data="count_player_1")
    )
    return builder.as_markup()
    
def get_report_panel() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(text="📕 Количество репортов", callback_data="count_report_1"),
        InlineKeyboardButton(text="👓 Репорты игроков", callback_data="read_report_1"),
        InlineKeyboardButton(text="Назад ◀️", callback_data="return_admin_panel_1")
    )
    return builder.as_markup()

def get_return_admin_panel() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(text="Назад ◀️", callback_data="return_admin_panel_1")
    )
    return builder.as_markup()