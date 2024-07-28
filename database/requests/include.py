from motor.core import AgnosticDatabase
from pymongo.database import Database
from json import dumps

from database.models.user import User
from database.models.report import Report

class IncludeUser:
    @staticmethod
    async def one_user_async(db: AgnosticDatabase, user: User):
        await db.user.insert_one(
            user.__dict__
        )


    @staticmethod
    def one_user(db: Database, user: User):
        db.user.insert_one(
            user.__dict__
        )

class IncludeReport:
    @staticmethod
    async def one_report_async(db: AgnosticDatabase, report: Report):
        await db.report.insert_one(
            report.__dict__
        )

    @staticmethod
    def one_report(db: Database, report: Report):
        db.report.insert_one(
            report.__dict__
        )