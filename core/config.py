from typing import Any, Optional
from json import dumps

class ConfigJSON:

    def __init__(self, data: dict) -> None:
        self.data = data

    def __str__(self) -> str:
        return dumps(self.data,
                     default=lambda o: o.__dict__)

    def _get(self, key: str) -> Optional[Any]:
        if key in self.data.keys():
            return self.data[key]
        return None