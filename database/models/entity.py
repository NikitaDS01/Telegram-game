from dataclasses import dataclass

from database.models.other import Actor

@dataclass
class Enemy(Actor):
    key_enemy: str