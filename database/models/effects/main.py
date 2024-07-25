from database.models.effects.config import EffectConfig
from database.models.effects.triggers import EffectTriggers, FactoryEffectTriggers

class Effect:
    def __init__(self, config: EffectConfig) -> None:
        self.name = config.name
        self.type = config.type
        self.step = config.step
        self.__triggers = dict[str, EffectTriggers]()
        for trigger in config.get_triggers():
            obj = FactoryEffectTriggers.get(trigger, config.get_json_trigger(trigger))
            self.__triggers[trigger] = obj

    def contain_trigger(self, name:str) -> bool:
        return name in self.__triggers.keys()
    
    def get_trigger(self, name:str) -> EffectTriggers | None:
        if self.contain_trigger(name):
            return self.__triggers[name]
        return None