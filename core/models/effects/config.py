from core.models.triggers.config import TriggerConfig
from core.type import TypeEffect
from core.config import ConfigJSON

### класс информации о эффекти
class EffectConfig(ConfigJSON):
    ID: str = 'id'
    NAME: str = 'name'
    TYPE: str = 'type'
    STEP: str = 'step'
    TRIGGERS: str = 'triggers'

    def __init__(self, data: dict) -> None:
        super().__init__(data)

    @property
    def id(self) -> str:
        value = self._get(EffectConfig.ID)
        if value is None: raise ValueError('не существует ключа id')
        return value
    

    @property
    def name(self) -> str:
        value = self._get(EffectConfig.NAME)
        if value is None: raise ValueError('не существует ключа name')
        return value
    

    @property
    def type(self) -> str:
        value = self._get(EffectConfig.TYPE)
        if value is None: raise ValueError('не существует ключа type')
        return value
    

    @property
    def step(self) -> int:
        value = self._get(EffectConfig.STEP)
        if value is None: raise ValueError('не существует ключа step')
        return value
    
    
    @property
    def triggers(self) -> list[TriggerConfig]:
        value = self._get(EffectConfig.TRIGGERS)
        if value is None: list()
        list_ = [TriggerConfig(data) for data in value]
        return list_
    


class CreateEffectConfig():
    @staticmethod
    def create(id: str, name: str, 
               type: int | TypeEffect, step: int,
               list_triggers: list[TriggerConfig] | None):
        dict = {
            EffectConfig.ID: id,
            EffectConfig.NAME: name,
            EffectConfig.STEP: step,
            EffectConfig.TYPE: type,
        }
        if not(list_triggers is None): dict[EffectConfig.TRIGGERS] = [trigger.data for trigger in list_triggers]
        return EffectConfig(dict)
