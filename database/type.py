from enum import IntEnum

class TypeAbility(IntEnum):
    Active = 1

class TypeDamage(IntEnum):
    Null = -1
    Fear = 0,
    Range = 1,
    Magic = 2