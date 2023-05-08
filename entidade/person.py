# vini
from abc import ABC, abstractmethod

class Person(ABC):
    @abstractmethod
    def __init__(self, name : str, id : int):
        if isinstance(name, str):
            self.__name = name
        if isinstance(id, int):
            self.__id = id
    
    @property
    def name(self):
        return self.__name
    @property
    def id(self):
        return self.__id
    
    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self.__name = name
    @id.setter
    def id(self, id):
        if isinstance(id, int):
            self.__id = id


