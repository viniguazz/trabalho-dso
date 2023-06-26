from abc import ABC, abstractmethod
from exception import InvalidNativeTypeException


class Person(ABC):
    @abstractmethod
    def __init__(self, name : str):
        if not isinstance(name, str):
            raise InvalidNativeTypeException(name, "str")
        self.__name = name
    
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise InvalidNativeTypeException(name, "str")
        self.__name = name    