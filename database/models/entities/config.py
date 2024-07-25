from database.config import ConfigJSON
from database.models.other import State

class EnemyConfig(ConfigJSON):
    def __init__(self, data: dict) -> None:
        super().__init__(data)
        
    @property
    def name(self) -> str:
        value = self._get('name')
        if value is None: raise ValueError('не существует ключа name')
        return value
    @property
    def state(self) -> State:
        value = self._get('state')
        if value is None: raise ValueError('не существует ключа state')
        return State.to_json(value)
    @property
    def drop(self) -> list[str]:
        value = self._get('drop')
        if value is None: return list[str]()
        return value
    @property
    def passiv_abilities(self) -> list[str]:
        value = self._get('passiv_abilities')
        if value is None: return list[str]()
        return value
    @property
    def active_abilities(self)  -> list[str]:
        value = self._get('active_abilities')
        if value is None: return list[str]()
        return value
    
class CreateEnemyConfig:

    @staticmethod
    def create(name: str, state: State, 
               drop = list(),
               pass_abil = list(),
               act_abil = list()):
        return EnemyConfig(
            data = {
                'name': name,
                'state': state,
                'drop': drop,
                'passiv_abilities': pass_abil,
                'active_abilities': act_abil
            }
        )