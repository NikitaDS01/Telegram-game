from core.config import ConfigJSON
from database.models.other import State
from database.models.config import Item

class EnemyConfig(ConfigJSON):
    ID: str = 'id'
    NAME: str = 'name'
    STATE: str = 'state'
    DROP: str = 'drop'
    ABILITIES ='abilities'

    def __init__(self, data: dict) -> None:
        super().__init__(data)
        
    
    @property
    def id(self) -> str:
        value = self._get(EnemyConfig.ID)
        if value is None: raise ValueError('не существует ключа id')
        return value
    

    @property
    def name(self) -> str:
        value = self._get(EnemyConfig.NAME)
        if value is None: raise ValueError('не существует ключа name')
        return value
    
    
    @property
    def default_state(self) -> State:
        value = self._get(EnemyConfig.STATE)
        if value is None: raise ValueError('не существует ключа state')
        return State.to_json(value)
    
    
    @property
    def drop(self) -> list[Item]:
        value = self._get(EnemyConfig.DROP)
        if value is None: return list[Item]()
        list_ = [Item.to_json(item) for item in value]
        return list_
    

    @property
    def abilities(self) -> list[str]:
        value = self._get(EnemyConfig.ABILITIES)
        if value is None: return list[str]()
        return value
    

    
class CreateEnemyConfig:
    @staticmethod
    def create(name: str, state: State, 
               drop: list[Item] = list(),
               pass_abil: list[str] = list(),
               act_abil: list[str] = list()):
        return EnemyConfig(
            data = {
                'name': name,
                'state': state,
                'drop': drop,
                'passiv_abilities': pass_abil,
                'active_abilities': act_abil
            }
        )