from abc import ABC, abstractmethod

# Для последствий эффектов 
class EffectConsequence(ABC):
    def __init__(self, 
                 name: str,
                 property: dict) -> None:
        self.name = name
        self.property = property 

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

# На что должен реагировать эффекты 
class EffectTriggers(ABC):
    def __init__(self, 
                 name: str,
                 property: dict, 
                 data: list[EffectConsequence]) -> None:
        self.name = name
        self.property = property 
        self.consequences = data

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



class FactoryEffectTriggers:
    @staticmethod
    def get(name: str, property: dict, 
            data: list[EffectConsequence]) -> EffectTriggers | None:
        templates = EffectTriggers.__subclasses__()
        for temp in templates:
            if name == temp.__name__:
                return temp(name, property, data)
        return None
    
class FactoryEffectConsequence:
    @staticmethod
    def get(name: str, data: dict) -> EffectConsequence | None:
        templates = EffectConsequence.__subclasses__()
        for temp in templates:
            if name == temp.__name__:
                return temp(name, data)
        return None
