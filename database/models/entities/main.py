from dataclasses import dataclass
from database.models.entities.config import EnemyConfig
from database.models.other import Actor
from database.models.items.main import Item

class Enemy:
    def __init__(self, config: EnemyConfig) -> None:
        self.key_name = config.name
        self.default_state = config.state
        self.drop = config.drop
        self.passiv_abilities = config.passiv_abilities
        self.active_abilities = config.active_abilities

    def get_battle_enemy(self):
        return BattleEnemy(
            key_name = self.key_name,
            state = self.default_state,
            drop = self.drop,
            passiv_abilities = self.passiv_abilities,
            active_abilities = self.active_abilities,
            current_effect = list()
        )
    
@dataclass
class BattleEnemy(Actor):
    key_name: str
    drop: list[Item]