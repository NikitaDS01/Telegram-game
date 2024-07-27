from core.models.abilities.config import AbilityConfig
from core.models.triggers.trigger import BaseTrigger, FactoryTriggers

class Ability:
    def __init__(self, config: AbilityConfig) -> None:
        self.name = config.name
        self.game_name = config.game_name
        self.type = config.type
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
    

    def __action_trigger(self, name:str):
        trigger = self.get_trigger(name)
        if trigger is None: return
        trigger.work()


    def on_damage(self, damage: int):
        trigger = self.get_trigger('OnDamage')
        if trigger is None: return
        #print(type(trigger))
        if trigger.damage > damage: return
        trigger.work()

