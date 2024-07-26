from core.config import ConfigJSON
from core.type import TypeAbility, TypeDamage
from core.models.abilities.triggers import OnDamageAbility, OnTestAbility

### класс информации о ability
class AbilityConfig(ConfigJSON): 
    def __init__(self, data: dict) -> None:
        super().__init__(data)

    @property
    def name(self) -> str:
        value = self._get('name')
        if value is None: raise ValueError('не существует ключа name')
        return value
    @property
    def game_name(self) -> str:
        value = self._get('game_name')
        if value is None: raise ValueError('не существует ключа game_name')
        return value
    @property
    def type(self) -> TypeAbility:
        value = self._get('type')
        if value is None: raise ValueError('не существует ключа type')
        return value
    
    @property
    def list_triggers(self) -> list[dict]:
        value = self._get('triggers')
        if value is None: list()
        return value

    def get_triggers(self):
        return list(self.data.keys())[2:]

    def get_json_trigger(self, name: str):
        value = self._get(name)
        return value
    
    @property
    def on_damage(self):
        value = self._get('OnDamageAbility')
        if value is None: return None
        return OnDamageAbility(value)
    
class CreateAbilityConfig():
    @staticmethod
    def create(name: str, game_name: str, type: int | TypeAbility, 
               onDamage: OnDamageAbility | None = None,
               onTest: OnTestAbility | None = None):
        dict = {
            'name': name,
            'game_name': game_name,
            'type': type,
        }
        if not(onDamage is None): dict['OnDamageAbility'] = onDamage.__dict__
        if not(onTest is None): dict['OnTestAbility'] = onTest.__dict__
        return AbilityConfig(dict)
    
    @staticmethod
    def create_on_test(value: int):
        return OnTestAbility(
            {
                'value': value,
            }
        )
    
    @staticmethod
    def create_on_damage(damage: int, type: int | TypeDamage):
        return OnDamageAbility(
            {
                'damage': damage,
                'type': type
            }
        )