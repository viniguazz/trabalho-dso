from abc import ABC, abstractmethod
import pickle


class DAO(ABC):
    
    def __init__(self, datasource=''):
        self.__datasource = datasource
        self.__cache = {}
    try:
        self.__load()
    except FileNotFoundError:
        self.__dump()

    def __dump(self):
        pickle.dump(self.__cache, open(self.__datasource, 'wb'))

    def __load(self):
        self.__cache = pickle.load(open(self.__datasource, 'rb'))

