from core.config import ConfigJSON

class DialogConfig(ConfigJSON):
    def __init__(self, data: dict) -> None:
        super().__init__(data)

    def __str__(self) -> str:
        return self.data.__str__()
    
    @property
    def name(self) -> str:
        value = self._get('name')
        if value is None: raise ValueError('не существует ключа name')
        return value
    @property
    def message(self) -> str:
        value = self._get('message')
        if value is None: raise ValueError('не существует ключа message')
        return value
    @property
    def answers(self) -> list[str]:
        value = self._get('answers')
        if value is None: list[str]()
        return value

class DialogBranchConfig(ConfigJSON):
    def __init__(self, data: dict) -> None:
        super().__init__(data)

    def __str__(self) -> str:
        return self.data.__str__()
    
    @property
    def name(self) -> str:
        value = self._get('name')
        if value is None: raise ValueError('не существует ключа name')
        return value
    
    @property
    def dialogs(self) -> list[DialogConfig]:
        values = self._get('dialogs')
        if values is None: return dict[int]()
        list_ = list()
        for value in values:
            list_.append(DialogConfig(value.get('data')))
        return list_
    
class CreateDialogsConfig:

    @staticmethod
    def create_dialog(name: str, message: str, answers: list[str]):
        return DialogConfig(
            data = {
                'name': name,
                'message': message,
                'answers': answers
            }
        )
    
    @staticmethod
    def create_branch(name: str, dialogs: list[DialogConfig]):
        json_dialogs = [dialog.data for dialog in dialogs]
        return DialogBranchConfig(
            data = {
                'name': name,
                'dialogs': json_dialogs
            }
        )