from abc import ABC, abstractmethod

from core.models.triggers.config import ConfigConsequence

class BaseConsequence(ABC):
    """
    Класс действий для триггера
    """
    def __init__(self, config: ConfigConsequence) -> None:
        self.name = config.name
        self.property = config.properties 


    @property
    def key(self):
        return self.name


    def get_property(self, name_property:str):
        if name_property in self.property.keys():
            return self.property[name_property]
        return None


    @abstractmethod
    def work(self):
        raise InterruptedError('word not')
    


class FactoryConsequence:
    @staticmethod
    def get_config(config: ConfigConsequence) -> BaseConsequence | None:
        consequences = BaseConsequence.__subclasses__()
        for consequence in consequences:
            if config.name == consequence.__name__:
                return consequence(config)
        return None


    @staticmethod
    def get(name: str, property: dict) -> BaseConsequence | None:
        consequences = BaseConsequence.__subclasses__()
        for consequence in consequences:
            if name == consequence.__name__:
                return consequence(ConfigConsequence({
                    "name": name, 
                    "property": property
                }))
        return None
    


class Print(BaseConsequence):
    def __init__(self, config: ConfigConsequence) -> None:
        super().__init__(config)

    @property
    def message(self):
        value = self.get_property('message')
        if value is None: raise ValueError('не существует ключа message')
        return value

    def work(self):
        print(f'print - {self.message}')