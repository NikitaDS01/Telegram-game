from dataclasses import dataclass

### класс Свойств
@dataclass
class Property:
    name: str
    value: int

    @staticmethod
    def convert(json:dict):
        return Property(
            name = json.get('name'),
            value = json.get('value'),
        )

@dataclass
### Класс для работы с основными характеристиками
class State:
    level: int
    max_health: int
    current_health: int
    
    @staticmethod
    @property
    def zero():
        return State(
            level = 1,
            max_health = 100,
            current_health = 100 
        )

    @staticmethod
    def to_json(data: dict):
        return State(
            level = data.get('level'),
            max_health = data.get('max_health'),
            current_health = data.get('current_health')
        )

@dataclass
class Actor:
    state: State # хар-ки персонажа
    current_effect: list[str] # Какие эффекты действуют
    passiv_abilities: list[str] # Список пассивных возможностей
    active_abilities: list[str] # Список активных возможностей

    ### Работа с ability

    def add_ability(self, data: str) -> bool:
        if data.type == "Passive":
            self.passiv_abilities.append(data)
        elif data.type == "Active":
            self.active_abilities.append(data)

    ### Работа с эффектами

    def add_effect(self, data: str) -> bool:
        self.current_effect.append(data)