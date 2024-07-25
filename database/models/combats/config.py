from database.config import ConfigJSON

class CombatConfig(ConfigJSON):
    def __init__(self, data: dict) -> None:
        super().__init__(data)
