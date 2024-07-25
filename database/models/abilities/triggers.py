from abc import ABC, abstractmethod

# Для последствий навыков 
class AbilityConsequence(ABC):
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

# На что должен реагировать навык 
class AbilityTriggers(ABC):
    def __init__(self, 
                 name: str,
                 property: dict, 
                 data: list[AbilityConsequence]) -> None:
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



class FactoryAbilityTriggers:
    @staticmethod
    def get(name: str, property: dict, 
            data: list[AbilityConsequence]) -> AbilityTriggers | None:
        templates = AbilityTriggers.__subclasses__()
        for temp in templates:
            if name == temp.__name__:
                return temp(name, property, data)
        return None
    
class FactoryAbilityConsequence:
    @staticmethod
    def get(name: str, data: dict) -> AbilityConsequence | None:
        templates = AbilityConsequence.__subclasses__()
        for temp in templates:
            if name == temp.__name__:
                return temp(name, data)
        return None


class OnActionAbility(AbilityTriggers):
    def __init__(self, 
                 name: str,
                 property: dict, 
                 data: list[AbilityConsequence]) -> None:
        super().__init__(name, property, data)


class OnDamageAbility(AbilityTriggers):
    def __init__(self, 
                 name: str,
                 property: dict, 
                 data: list[AbilityConsequence]) -> None:
        super().__init__(name, property, data)

    @property
    def time(self):
        value = self.get_property('time')
        if value is None: raise ValueError('не существует ключа time')
        return value

class OnTestAbility(AbilityTriggers):
    def __init__(self, 
                 name: str,
                 property: dict,  
                 data: list[AbilityConsequence]) -> None:
        super().__init__(name, property, data)


class Print(AbilityConsequence):
    def __init__(self, 
                 name: str,
                 property: dict) -> None:
        super().__init__(name, property)

    @property
    def message(self):
        value = self.get_property('message')
        if value is None: raise ValueError('не существует ключа message')
        return value

    def work(self):
        print(f'print - {self.message}')