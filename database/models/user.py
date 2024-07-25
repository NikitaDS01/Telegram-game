from dataclasses import dataclass
from database.models.items.main import Item
from database.models.other import Actor, State

@dataclass
class StateUser:
    level: int
    max_health: int
    current_health: int

    @staticmethod
    @property
    def zero():
        return StateUser(
            level = 1,
            max_health = 100,
            current_health = 100 
        )


@dataclass
class PartsUser:
    weapon_right: Item
    weapon_left: Item

@dataclass
class User(Actor):
    telegram_id: int 
    role: str
    state_user: StateUser # хар-ки персонажа
    parametry: dict[str] # Локальные параметры 
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
    def get_item(self, data: str | Item) -> Item | None:
        txt = data
        if isinstance(data, Item):
            txt = data.name
        for item in self.inventory:
            if item.name == txt:
                return item
        return None
        
    def change_count_item(self, name: str, count: int):
        self.add_item(Item(name, count))

    def add_item(self, data: Item) -> bool:
        if(data < 0):
            return False

        item = self.get_item(data = data)
        if item is None:
            self.inventory.append(data)
        else:
            item.count += data.count
        return True

    @staticmethod
    def create_zero_user(number: int, role: str):
        return User(telegram_id = number,
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
