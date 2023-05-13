# vini
from abc import ABC, abstractmethod
from tipo_errado_exception import TipoErradoException

class Person(ABC):
    
    id = 0
    
    @abstractmethod
<<<<<<< HEAD
    def __init__(self, name : str):
        if isinstance(name, str):
            self.__name = name
        self.__id = id
        id += 1

=======
    def __init__(self, name : str, id : int):
        if not isinstance(name, str):
            raise TipoErradoException
        if not isinstance(id, int):
            raise TipoErradoException
        self.__name = name
        self.__id = id
    
>>>>>>> 3bd7befde95dd119262c0ed31511eb7b64218f4e
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