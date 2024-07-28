from dataclasses import dataclass
from enum import IntEnum
import datetime

class StatusReport(IntEnum):
    New = 0
    Read = 1
    Completed = 2

@dataclass
class Report:
    user_id:int
    create_report:datetime
    message:str
    status: StatusReport

    @staticmethod
    def to_json(json: dict):
        return Report(user_id = json.get('user_id'),
                      create_report=json.get('create_report'),
                      message = json.get('message'),
                      status = json.get('status'))