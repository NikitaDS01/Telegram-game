from core.models.entities.config import EnemyConfig

class Enemy:
    def __init__(self, config: EnemyConfig) -> None:
        self.key_name = config.name
        self.default_state = config.default_state
        self.drop = config.drop
        self.passiv_abilities = config.passiv_abilities
        self.active_abilities = config.active_abilities