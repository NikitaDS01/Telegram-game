from datetime import datetime
from motor.core import AgnosticDatabase as MDB
from database import models

async def one_report(db: MDB, report: models.report.Report):
    await db.report.insert_one(
        dict(
            user_id = report.user_id,
            create_report = report.create_report,
            message = report.message,
            status = report.status
        )
    )

async def one_user(db: MDB, user: models.user.User):
    await db.user.insert_one(
        dict(
            _id = user.telegram_id,
            role = user.status,
            money = user.money,
            inventory = user.inventory,
            abilities = user.abilities,
            property = user.properties,
            effect = user.effects,
            create_user = datetime.now(),
            update_user = datetime.now()
        )
    )