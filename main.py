import asyncio
from loguru import logger as log
from handlers import setup_routers
from aiogram import Bot
from aiogram import Dispatcher
from motor.motor_asyncio import AsyncIOMotorClient
from config_reader import config

async def start_bot():
    log.info("Bot start")

async def stop_bot():
    log.info("Bot stop")

def registry_model():
    pass

async def main() -> None:

    registry_model()

    log.add('log\\debug.log', format="{time} {level} {message}", level = "DEBUG", rotation = "1 MB")

    bot = Bot(config.TOKEN.get_secret_value())
    dp = Dispatcher()

    cluster = AsyncIOMotorClient(config.DATABASE_URL.get_secret_value())
    mdb = cluster.games

    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    dp.include_router(setup_routers())
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, db=mdb)

if(__name__ == "__main__"):
    asyncio.run(main(), debug=True)
