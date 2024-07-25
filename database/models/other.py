from dataclasses import dataclass
from database.models.effects.config import EffectConfig
from database.models.abilities.config import AbilityConfig

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
    current_effect: list[EffectConfig] # Какие эффекты действуют
    passiv_abilities: list[AbilityConfig] # Список пассивных возможностей
    active_abilities: list[AbilityConfig] # Список активных возможностей

    ### Работа с ability

    def add_ability(self, data: AbilityConfig) -> bool:
        if data.type == "Passive":
            self.passiv_abilities.append(data)
        elif data.type == "Active":
            self.active_abilities.append(data)

    ### Работа с эффектами

    def add_effect(self, data: EffectConfig) -> bool:
        self.current_effect.append(data)