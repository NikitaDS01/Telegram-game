from core.models.triggers.config import ConfigTrigger
from core.models.triggers.trigger import FactoryTriggers
from core.models.abilities.main import Ability
from core.models.abilities.config import AbilityConfig, CreateAbilityConfig

def test1():
    cons1 = {
        "name": "Print",
        "property": {
            "message": "Test world!"
        }
    }
    cons2 = {
        "name": "Print",
        "property": {
            "message": "Просто тест!"
        }
    }
    dict_ = {
        "name": "OnDamage",
        "property": {
            "damage": 100
        },
        "consequences": [
            cons1,
            cons2
        ]
    }
    trigger_config = ConfigTrigger(dict_)
    ability_config = CreateAbilityConfig.create("test_1", "Тестовое", "1", [trigger_config])
    ability = Ability(ability_config)
    print(ability.__dict__)
    ability.on_damage(150)
    
    #registry._write(branch1)

# Point(x=1436, y=519)
# Point(x=1404, y=65)
# Point(x=1256, y=163)

    
if(__name__ == "__main__"):
    test1()