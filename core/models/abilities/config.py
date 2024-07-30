from core.config import ConfigJSON
from core.type import TypeAbility
from core.models.triggers.config import TriggerConfig

### класс информации о ability
class AbilityConfig(ConfigJSON): 
    ID: str = 'id'
    NAME: str = 'name'
    TYPE: str = 'type'
    TRIGGERS: str = 'triggers'

    def __init__(self, data: dict) -> None:
        super().__init__(data)

    @property
    def id(self) -> str:
        value = self._get(AbilityConfig.ID)
        if value is None: raise ValueError('не существует ключа id')
        return value
    

    @property
    def name(self) -> str:
        value = self._get(AbilityConfig.NAME)
        if value is None: raise ValueError('не существует ключа name')
        return value
    

    @property
    def type(self) -> TypeAbility:
        value = self._get(AbilityConfig.TYPE)
        if value is None: raise ValueError('не существует ключа type')
        return value
    
    
    @property
    def triggers(self) -> list[TriggerConfig]:
        value = self._get(AbilityConfig.TRIGGERS)
        if value is None: list()
        list_ = [TriggerConfig(data) for data in value]
        return list_
    

    
class CreateAbilityConfig():
    @staticmethod
    def create(id: str, name: str, type: int | TypeAbility, 
               list_triggers: list[TriggerConfig] | None):
        dict = {
            AbilityConfig.ID: id,
            AbilityConfig.NAME: name,
            AbilityConfig.TYPE: type,
        }
        if not(list_triggers is None): dict[AbilityConfig.TRIGGERS] = [trigger.data for trigger in list_triggers]
        return AbilityConfig(dict)