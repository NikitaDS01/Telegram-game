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
    def setting(self) -> ItemSetting:
        value = self._get('setting')
        if value is None: raise ValueError('не существует ключа setting')
        return ItemSetting.to_json(value)
    
    
    @property
    def abilities(self) -> list[str]:
        value = self._get('abilities')
        if value is None: return list()
        if isinstance(value, list): raise ValueError('abilities не является списком')
        return list[str]()
        #for v in value: abil.append(ListAbilityZ.get_json(v))
        #return abil