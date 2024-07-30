from abc import ABC

from core.models.triggers.consequence import FactoryConsequence
from core.models.triggers.config import TriggerConfig

class BaseTrigger(ABC):
    """
    Класс триггера
    """
    def __init__(self, config: TriggerConfig) -> None:
        self.name = config.name
        self.property = config.properties 
        self.consequences = [FactoryConsequence.get_config(conseq) for conseq in config.consequences]

    def get_property(self, name_property:str):
        if name_property in self.property.keys():
            return self.property[name_property]
        return None

    @property
    def key(self):
        return self.name

    def work(self):
        for consequence in self.consequences:
            consequence.work()



class FactoryTriggers:
    @staticmethod
    def get_config(config: TriggerConfig) -> BaseTrigger | None:
        triggers = BaseTrigger.__subclasses__()
        for trigger in triggers:
            if config.name == trigger.__name__:
                return trigger(config)
        return None


    @staticmethod
    def get(name: str, 
            property: dict, 
            data: list[dict]) -> BaseTrigger | None:
        triggers = BaseTrigger.__subclasses__()
        for trigger in triggers:
            if name == trigger.__name__:
                return trigger(TriggerConfig({
                    "name": name, 
                    "property": property, 
                    "consequences": data
                }))
        return None
    

class OnDamage(BaseTrigger):
    def __init__(self, config: TriggerConfig) -> None:
        super().__init__(config)

    @property
    def damage(self):
        value = self.get_property('damage')
        if value is None: raise ValueError('не существует ключа damage')
        return value
