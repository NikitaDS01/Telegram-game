from core.models.effects.config import EffectConfig
from core.models.triggers.trigger import BaseTrigger, FactoryTriggers

class Effect:
    def __init__(self, config: EffectConfig) -> None:
        self.name = config.name
        self.type = config.type
        self.step = config.step
        self.__triggers = dict[str, BaseTrigger]()
        for config_trig in config.triggers:
            trigger = FactoryTriggers.get_config(config_trig)
            if not(trigger is None):
                self.__triggers[trigger.name] = trigger

    def contain_trigger(self, name:str) -> bool:
        return name in self.__triggers.keys()
    


    def get_trigger(self, name:str) -> BaseTrigger | None:
        if self.contain_trigger(name):
            return self.__triggers[name]
        return None