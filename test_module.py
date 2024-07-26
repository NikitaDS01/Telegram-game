from database.models.abilities.config import AbilityConfig
from database.models.abilities.main import Ability
from web.website import start_website

def test1():
    dict_trigger = {
        "name": "OnDamageAbility",
        "property": {
            "time": 1
        },
        "consequence": [
            {
                "name": "Print",
                "property": {
                    "message": "Hello World!"}
                }
            ]
    }
    dict_ability = {
        "name": "test_ability_1",
        "game_name": "Тестовый навык",
        "type": "active",
        "triggers": [dict_trigger]
    }
    config = AbilityConfig(dict_ability)
    abil = Ability(config)
    print(abil.__dict__)
    abil.on_damage()
    #registry._write(branch1)

# Point(x=1436, y=519)
# Point(x=1404, y=65)
# Point(x=1256, y=163)

    
if(__name__ == "__main__"):
    start_website()