from motor.core import AgnosticDatabase as MDB
from database.models.report import Report


async def one_user(db: MDB, filter: str = { }):
    return await db.user.find_one(filter)

async def many_user(db: MDB, filter: str = { }, skip:int = 0, limit:int = 0):
    return await db.user.find(filter).skip(skip).limit(limit)

async def one_report(db: MDB, filter: str = { }):
    return await db.report.find_one(filter)

async def many_report(db: MDB, filter: str = { }, skip:int = 0, limit:int = 0):
    return await db.report.find(filter).skip(skip).limit(limit)

async def count_report(db: MDB, filter: str = { }):
    return await db.report.count_documents(filter)