from database.config import ConfigJSON
from dataclasses import dataclass

@dataclass
class LocationSetting:
    day_night_cycle: bool = False

    @staticmethod
    def to_json(data: dict):
        return LocationSetting(
            day_night_cycle = data.get('day_night_cycle')
        )

class LocationConfig(ConfigJSON):
    # enemy_spawn: dict[str, float]
    # day_night_cycle: bool
    def __init__(self, data: dict) -> None:
        super().__init__(data)

    @property
    def name(self) -> str:
        value = self._get('name')
        if value is None: raise ValueError('не существует ключа name')
        return value
    @property
    def setting(self) -> LocationSetting:
        value = self._get('type')
        if value is None: raise ValueError('не существует ключа setting')
        return LocationSetting.to_json(value)
    @property
    def type(self) -> str:
        value = self._get('type')
        if value is None: raise ValueError('не существует ключа type')
        return value
    @property
    def terrain(self) -> str:
        value = self._get('terrain')
        if value is None: raise ValueError('не существует ключа terrain')
        return value
    @property
    def relation(self) -> list[str]:
        value = self._get('relation')
        if value is None: raise ValueError('не существует ключа relation')
        return value
    