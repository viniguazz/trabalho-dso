# vini
from abc import ABC, abstractmethod

class Person(ABC):
    
    id = 0
    
    @abstractmethod
    def __init__(self, name : str):
        if isinstance(name, str):
            self.__name = name
        self.__id = id
        id += 1

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


