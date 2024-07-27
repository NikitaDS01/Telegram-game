from core.registry.base_registry import BaseRegister, FileInitRegistry

class RegistryItems(BaseRegister):
    def __init__(self, path: str) -> None:
        super().__init__(path, FileInitRegistry)


    def _save_object(self, json: dict):
        pass