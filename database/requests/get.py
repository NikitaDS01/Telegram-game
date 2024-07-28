from motor.core import AgnosticDatabase
from pymongo.database import Database

from database.models.report import Report

class GetUser:
    @staticmethod
    async def one_user_async(db: AgnosticDatabase, filter: str = { }):
        return await db.user.find_one(filter)


    @staticmethod
    async def many_user_async(db: AgnosticDatabase, filter: str = { }, skip:int = 0, limit:int = 0):
        return await db.user.find(filter).skip(skip).limit(limit)
    

    @staticmethod
    async def one_use_async(db: Database, filter: str = { }):
        return await db.user.find_one(filter)


    @staticmethod
    def many_user(db: Database, filter: str = { }, skip:int = 0, limit:int = 0):
        return db.user.find(filter).skip(skip).limit(limit)


class GetReport:
    @staticmethod
    async def one_report_async(db: AgnosticDatabase, filter: str = { }):
        return await db.report.find_one(filter)
    

    @staticmethod
    def one_report(db: Database, filter: str = { }):
        return db.report.find_one(filter)


    @staticmethod
    async def many_report_async(db: AgnosticDatabase, filter: str = { }, skip:int = 0, limit:int = 0):
        return await db.report.find(filter).skip(skip).limit(limit)


    @staticmethod
    def many_report(db: Database, filter: str = { }, skip:int = 0, limit:int = 0):
        return db.report.find(filter).skip(skip).limit(limit)


    @staticmethod
    async def count_report_async(db: AgnosticDatabase, filter: str = { }):
        return await db.report.count_documents(filter)


    @staticmethod
    def count_report(db: Database, filter: str = { }):
        return db.report.count_documents(filter)