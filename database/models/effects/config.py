from database.config import ConfigJSON

class CreateEffectConfig():
    @staticmethod
    def create(name: str, type: str, step: int):
        dict = {
            'name': name,
            'type': type,
            'step': step,
        }
        return EffectConfig(dict)
### класс информации о эффекти
class EffectConfig(ConfigJSON):
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
    def type(self) -> str:
        value = self._get('type')
        if value is None: raise ValueError('не существует ключа type')
        return value
    @property
    def step(self) -> int:
        value = self._get('type')
        if value is None: raise ValueError('не существует ключа step')
        return value
    
    def get_triggers(self):
        return list(self.data.keys())[2:]

    def get_json_trigger(self, name: str):
        value = self._get(name)
        return value