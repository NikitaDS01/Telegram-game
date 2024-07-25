from database.config import ConfigJSON
from database.models.abilities.config import AbilityConfig

class ItemConfig(ConfigJSON):
    def __init__(self, data: dict) -> None:
        super().__init__(data)

    @property
    def name(self) -> str:
        value = self._get('name')
        if value is None: raise ValueError('не существует ключа name')
        return value
    @property
    def type(self) -> str:
        value = self._get('type')
        if value is None: raise ValueError('не существует ключа type')
        return value
    @property
    def cost(self) -> str:
        value = self._get('cost')
        if value is None: return 0
        return value
    @property
    def max_count(self) -> int:
        value = self._get('max_count')
        if value is None: return 1
        return value
    @property
    def abilities(self) -> list[str]:
        value = self._get('abilities')
        if value is None: return list()
        if isinstance(value, list): raise ValueError('abilities не является списком')
        return list[str]()
        #for v in value: abil.append(ListAbilityZ.get_json(v))
        #return abil