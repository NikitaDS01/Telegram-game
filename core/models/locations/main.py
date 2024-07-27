from core.models.locations.config import LocationConfig

class Location:
    def __init__(self, config: LocationConfig) -> None:
        self.name = config.name
        self.setting = config.setting
        self.type = config.type
        self.terrain = config.terrain
        self.relation = config.relation

    
    @property
    def _random_key(self):
        return self.setting.random_key