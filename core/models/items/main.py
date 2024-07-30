from core.models.items.config import ItemConfig

class Item:
    """
    Класс предметов
    """
    def __init__(self, config: ItemConfig):
        self.name = config.name
        self.type_item = config.type
        self.cost = config.cost
        self.abilities = config.abilities