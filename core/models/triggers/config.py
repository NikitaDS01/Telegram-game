from core.config import ConfigJSON

class ConsequenceConfig(ConfigJSON):
    ID: str = 'id'
    PROPERTIES: str = 'properties'

    def __init__(self, data: dict) -> None:
        super().__init__(data)

    
    @property
    def id(self) -> str:
        value = self._get(ConsequenceConfig.ID)
        if value is None: raise ValueError('не существует ключа id')
        return value
    

    @property
    def properties(self) -> dict:
        value = self._get(ConsequenceConfig.PROPERTIES)
        if value is None: dict()
        return value
    


class TriggerConfig(ConfigJSON):
    ID: str = 'id'
    PROPERTIES: str = 'properties'
    CONSEQUENCES: str = 'consequences'

    def __init__(self, data: dict) -> None:
        super().__init__(data)

    
    @property
    def id(self) -> str:
        value = self._get(TriggerConfig.ID)
        if value is None: raise ValueError('не существует ключа id')
        return value
    

    @property
    def properties(self) -> dict:
        value = self._get(TriggerConfig.PROPERTIES)
        if value is None: dict()
        return value
    

    @property
    def consequences(self) -> list[ConsequenceConfig]:
        value = self._get(TriggerConfig.CONSEQUENCES)
        if value is None: list()
        list_ = [ConsequenceConfig(config) for config in value]
        return list_