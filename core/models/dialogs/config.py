from dataclasses import dataclass

from core.config import ConfigJSON

@dataclass
class Answer:
    value: str
    next_dialog: str

    @staticmethod
    def to_json(data: dict):
        return Answer(
            value = data.get('value'),
            next_dialog = data.get('next_dialog')
        )

class DialogConfig(ConfigJSON):
    ID: str = 'id'
    MESSAGE: str = 'message'
    ANSWERS: str = 'answers'

    def __init__(self, data: dict) -> None:
        super().__init__(data)
    

    @property
    def name(self) -> str:
        value = self._get(DialogConfig.ID)
        if value is None: raise ValueError('не существует ключа id')
        return value
    

    @property
    def message(self) -> str:
        value = self._get(DialogConfig.MESSAGE)
        if value is None: raise ValueError('не существует ключа message')
        return value
    

    @property
    def answers(self) -> list[str]:
        value = self._get(DialogConfig.ANSWERS)
        if value is None: list[str]()
        list_ = [Answer.to_json(answer) for answer in value]
        return list_
    


class DialogBranchConfig(ConfigJSON):
    ID: str = 'id'
    DIALOGS: str = 'dialogs'

    def __init__(self, data: dict) -> None:
        super().__init__(data)
    

    @property
    def name(self) -> str:
        value = self._get(DialogBranchConfig.ID)
        if value is None: raise ValueError('не существует ключа id')
        return value
    

    @property
    def dialogs(self) -> list[DialogConfig]:
        values = self._get(DialogBranchConfig.DIALOGS)
        if values is None: return dict[int]()
        list_ = [DialogConfig(config) for config in values]
        return list_
    


class CreateDialogsConfig:
    @staticmethod
    def create_dialog(id: str, message: str, answers: list[str]):
        return DialogConfig(
            data = {
                DialogConfig.ID: id,
                DialogConfig.MESSAGE: message,
                DialogConfig.ANSWERS: answers
            }
        )
    
    @staticmethod
    def create_branch(id: str, dialogs: list[DialogConfig]):
        json_dialogs = [dialog.data for dialog in dialogs]
        return DialogBranchConfig(
            data = {
                DialogBranchConfig.ID: id,
                DialogBranchConfig.DIALOGS: json_dialogs
            }
        )