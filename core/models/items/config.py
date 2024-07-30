from core.models.abilities.config import AbilityConfig
from dataclasses import dataclass
from core.config import ConfigJSON

@dataclass
class ItemSetting:
    max_count: int = 1


    @staticmethod
    def to_json(data: dict):
        return ItemSetting(
            max_count = data.get('max_count')
        )


class ItemConfig(ConfigJSON):
    """
    Класс для хранения конфигураций предметов
    """
    ID: str = 'id'
    NAME: str = 'name'
    TYPE: str = 'type'
    SETTING: str = 'setting'
    ABILITIES ='abilities'

    def __init__(self, data: dict) -> None:
        super().__init__(data)

    @property
    def id(self) -> str:
        value = self._get(ItemConfig.ID)
        if value is None: raise ValueError('не существует ключа id')
        return value


    @property
    def name(self) -> str:
        value = self._get(ItemConfig.NAME)
        if value is None: raise ValueError('не существует ключа name')
        return value
    
    
    @property
    def type(self) -> str:
        value = self._get(ItemConfig.TYPE)
        if value is None: raise ValueError('не существует ключа type')
        return value
    

    @property
    def setting(self) -> ItemSetting:
        value = self._get(ItemConfig.SETTING)
        if value is None: raise ValueError('не существует ключа setting')
        return ItemSetting.to_json(value)
    
    
    @property
    def abilities(self) -> list[str]:
        value = self._get(ItemConfig.ABILITIES)
        if value is None: return list()
        if isinstance(value, list): raise ValueError('abilities не является списком')
        list_ = [AbilityConfig(data) for data in value]
        return list_