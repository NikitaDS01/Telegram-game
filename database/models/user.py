from dataclasses import dataclass
from enum import IntEnum

from database.models.config import Item
from database.models.other import Actor, State

class Role(IntEnum):
    Simple = 0
    Admin = 1

@dataclass
class StateUser:
    Strength: int 
    Agility: int

    @staticmethod
    @property
    def zero():
        return StateUser(
            Strength = 1,
            Agility = 100
        )
    

@dataclass
class PartsUser:
    weapon_right: Item
    weapon_left: Item

@dataclass
class User(Actor):
    telegram_id: int 
    role: Role
    state_user: StateUser # хар-ки персонажа
    parametries: dict[str] # Локальные параметры 
    money: list[int] # деньги игрока
    inventory: list[Item] 

    ### Работа с переменными

    @property
    def max_health(self) -> int:
        return self.state.max_health
    
    @property
    def health(self) -> int:
        return self.state.current_health


    ### Работа с предметами
    def get_item(self, name: str) -> Item | None:
        for item in self.inventory:
            if item.name == name:
                return item
        return None


    def add_item(self, name: str, count: int) -> bool:
        if(count < 0):
            return False

        item = self.get_item(name = name)
        if item is None:
            self.inventory.append(Item(name, count))
        else:
            if item.count + count < 0:
                return False
            item.count += count
        return True


    @staticmethod
    def create_zero_user(id: int, role: int | Role):
        return User(telegram_id = id,
                    role = role,
                    current_effect = list(),
                    passiv_abilities = list(),
                    active_abilities = list(),
                    parametry = dict(),
                    money = list(),
                    inventory = list(),
                    state = State.zero,
                    state_user = StateUser.zero
                    )
