from core.config import ConfigJSON
from dataclasses import dataclass

@dataclass
class LocationSetting:
    day_night_cycle: bool = False
    random_key: int


    @staticmethod
    def to_json(data: dict):
        return LocationSetting(
            day_night_cycle = data.get('day_night_cycle'),
            random_key = data.get('random_key')
        )



class LocationConfig(ConfigJSON):
    ID: str = 'id'
    NAME: str = 'name'
    TYPE: str = 'type'
    SETTING: str = 'setting'
    TERRAIN = 'terrain'
    RELATION = 'relation'
    # ABILITIES ='abilities'

    def __init__(self, data: dict) -> None:
        super().__init__(data)

    @property
    def id(self) -> str:
        value = self._get(LocationConfig.ID)
        if value is None: raise ValueError('не существует ключа id')
        return value


    @property
    def name(self) -> str:
        value = self._get(LocationConfig.NAME)
        if value is None: raise ValueError('не существует ключа name')
        return value
    

    @property
    def setting(self) -> LocationSetting:
        value = self._get(LocationConfig.SETTING)
        if value is None: raise ValueError('не существует ключа setting')
        return LocationSetting.to_json(value)
    

    @property
    def type(self) -> str:
        value = self._get(LocationConfig.TYPE)
        if value is None: raise ValueError('не существует ключа type')
        return value
    

    @property
    def terrain(self) -> str:
        value = self._get(LocationConfig.TERRAIN)
        if value is None: raise ValueError('не существует ключа terrain')
        return value
    

    @property
    def relation(self) -> list[str]:
        value = self._get(LocationConfig.RELATION)
        if value is None: raise ValueError('не существует ключа relation')
        return value
    