from aiogram import Router
from . import bot_commands
from . import admin_commands

def setup_routers() -> Router:
    current_rounter = Router()

    current_rounter.include_router(bot_commands.router)
    current_rounter.include_router(admin_commands.router)
    return current_rounter