from dataclasses import dataclass

@dataclass
class Item:
    key: str
    count: int

    @staticmethod
    def to_json(data: dict):
        return Item(
            key = data.get('key'),
            count = data.get('count')
        )

@dataclass
class Effect:
    key: str
    step: int