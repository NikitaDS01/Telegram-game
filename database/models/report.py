import datetime
from dataclasses import dataclass

@dataclass
class Report:
    user_id:int
    create_report:datetime
    message:str
    status: str

    @staticmethod
    def convert(json: dict):
        return Report(user_id = json.get('user_id'),
                      create_report=json.get('create_report'),
                      message = json.get('message'),
                      status = json.get('status'))
