from core.models.entities.config import EnemyConfig

class Enemy:
    def __init__(self, config: EnemyConfig) -> None:
        self.id = config.id
        self.name = config.name
        self.default_state = config.default_state
        self.drop = config.drop
        self.abilities = config.abilities