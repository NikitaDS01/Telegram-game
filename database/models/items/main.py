from database.models.items.config import ItemConfig

class Item:
    def __init__(self, config: ItemConfig):
        self.name = config.name
        self.type_item = config.type
        self.cost = config.cost
        self.count = config.count
        self.abilities = config.abilities