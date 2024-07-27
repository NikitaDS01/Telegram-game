from core.config import ConfigJSON
from core.type import TypeAbility
from core.models.triggers.config import ConfigTrigger

### класс информации о ability
class AbilityConfig(ConfigJSON): 
    def __init__(self, data: dict) -> None:
        super().__init__(data)

    @property
    def name(self) -> str:
        value = self._get('name')
        if value is None: raise ValueError('не существует ключа name')
        return value
    

    @property
    def game_name(self) -> str:
        value = self._get('game_name')
        if value is None: raise ValueError('не существует ключа game_name')
        return value
    

    @property
    def type(self) -> TypeAbility:
        value = self._get('type')
        if value is None: raise ValueError('не существует ключа type')
        return value
    
    
    @property
    def triggers(self) -> list[ConfigTrigger]:
        value = self._get('triggers')
        if value is None: list()
        list_ = [ConfigTrigger(data) for data in value]
        return list_
    

    
class CreateAbilityConfig():
    @staticmethod
    def create(name: str, game_name: str, type: int | TypeAbility, 
               list_triggers: list[ConfigTrigger] | None):
        dict = {
            'name': name,
            'game_name': game_name,
            'type': type,
        }
        if not(list_triggers is None): dict['triggers'] = [trigger.data for trigger in list_triggers]
        return AbilityConfig(dict)