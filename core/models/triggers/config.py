from core.config import ConfigJSON

class ConfigConsequence(ConfigJSON):
    def __init__(self, data: dict) -> None:
        super().__init__(data)

    
    @property
    def name(self) -> str:
        value = self._get('name')
        if value is None: raise ValueError('не существует ключа name')
        return value
    

    @property
    def properties(self) -> dict:
        value = self._get('property')
        if value is None: dict()
        return value
    


class ConfigTrigger(ConfigJSON):
    def __init__(self, data: dict) -> None:
        super().__init__(data)

    
    @property
    def name(self) -> str:
        value = self._get('name')
        if value is None: raise ValueError('не существует ключа name')
        return value
    

    @property
    def properties(self) -> dict:
        value = self._get('property')
        if value is None: dict()
        return value
    

    @property
    def consequences(self) -> list[ConfigConsequence]:
        value = self._get('consequences')
        if value is None: list()
        list_ = [ConfigConsequence(config) for config in value]
        return list_