from core.models.abilities.config import AbilityConfig
from core.models.abilities.triggers import AbilityTriggers, FactoryAbilityTriggers, FactoryAbilityConsequence

class Ability:
    def __init__(self, config: AbilityConfig) -> None:
        self.name = config.name
        self.game_name = config.game_name
        self.type = config.type
        self.__triggers = dict[str, AbilityTriggers]()
        for trigger in config.list_triggers:
            list_consequence = list()
            for consequence in trigger.get('consequence'):
                obj_conseq = FactoryAbilityConsequence.get(consequence.get('name'),
                                                           consequence.get('property'))
                list_consequence.append(obj_conseq)
                print("object consequence - ", obj_conseq)
            obj = FactoryAbilityTriggers.get(trigger.get('name'),
                                             trigger.get('property'),
                                             list_consequence)
            self.__triggers[obj.key] = obj

    def contain_trigger(self, name:str) -> bool:
        return name in self.__triggers.keys()
    
    def get_trigger(self, name:str) -> AbilityTriggers | None:
        if self.contain_trigger(name):
            return self.__triggers[name]
        return None
    
    def __action_trigger(self, name:str):
        trigger = self.get_trigger(name)
        if trigger is None: return
        trigger.work()

    def on_action(self):
        self.__action_trigger('OnActionAbility')

    def on_damage(self):
        self.__action_trigger('OnDamageAbility')

    def on_test(self):
        self.__action_trigger('OnTestAbility')
