# vini
from abc import ABC, abstractmethod
from tipo_errado_exception import TipoErradoException

class Person(ABC):
    
    id = 0
    
    @abstractmethod
    def __init__(self, name : str, id : int):
        if not isinstance(name, str):
            raise TipoErradoException
        if not isinstance(id, int):
            raise TipoErradoException
        self.__name = name
        self.__id = id
    
    @property
    def name(self):
        return self.__name
    @property
    def id(self):
        return self.__id
    
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TipoErradoException
        self.__name = name    
            
    @id.setter
    def id(self, id):
        if not isinstance(id, int):
            raise TipoErradoException
        self.__id = id