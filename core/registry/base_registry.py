from abc import ABC, abstractmethod
from core.config import ConfigJSON
from typing import Optional, Any
from os import path, listdir
import json

class InitRegistry(ABC):
    pass

class FileInitRegistry(InitRegistry):
    def __init__(self, data: str) -> None:
        if path.isdir(data) == False:
            raise FileNotFoundError(str.format("Не существуют пути: {0}", data))
        self.list = listdir(data)
        self.numb = 0


    @property
    def max(self):
        return len(self.list)


    def __iter__(self):
        return self
    
    
    def __next__(self):
        if self.numb >= self.max:
            raise StopIteration
        else:
            self.numb += 1
            abil_path = self.l[self.numb - 1]
            new_path = self.__path + '\\' + abil_path
            file = open(new_path, 'r')
            file.close()
            return json.loads(file.read())
        


class BaseRegister(ABC):

    # __path: str = 'data\\abilities'
    # __dict: dict[str, Ability] = dict()

    def __init__(self, path: str, type_reg) -> None:
        self.__type_reg = type_reg
        self.__path = path
        self.__dict = dict[str]()
        self._is_init = False


    def __str__(self) -> str:
        return self.__dict.__str__()


    def init(self):
        for abil in self.__type_reg(self.__path):
            self.__dict[abil.get('name')] = self._save_object(abil)
        self._is_init = True

    
    @abstractmethod
    def _save_object(self, json: dict):
        """Сonverts an object from 
        JSON to config, and then 
        to a register object"""
        raise IndentationError('Not save_object')


    def get(self, name: str) -> Optional[Any]:
        if self._is_init == False: raise SystemError(str.format("Not init registry: {0}", self.__path))

        if name in self.__dict.keys():
            return self.__dict[name]
        return None


    def _write(self, config: ConfigJSON):
        if path.isdir(self.__path) == False:
            raise FileNotFoundError(str.format("Не существуют пути: {0}", self.__path))

        new_path = self.__path + '\\' + config.name + '.json'
        if path.isfile(new_path) == True:
            raise FileNotFoundError(str.format("Данный путь существует: {0}", self.__path))
        
        str_json = json.dumps(config.data,
                              default=lambda o: o.__dict__)
        file = open(new_path, 'w')
        file.write(str_json)
        file.close()
