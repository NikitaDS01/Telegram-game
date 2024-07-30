from loguru import logger as log
from motor.motor_asyncio import AsyncIOMotorClient
from flask import Flask
from flask_restful import Resource, Api, reqparse

from config_reader import config

app = Flask(__name__)
mdb = AsyncIOMotorClient(config.DATABASE_URL.get_secret_value())
api = Api(app)

if __name__ == "__main__":
    log.info('Start api')

