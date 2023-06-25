from abc import ABC, abstractmethod
import pickle


class DAO(ABC):

    def __init__(self, datasource=''):
        self.__datasource = datasource
        self.__cache = {}
        try:
            self.__load()
        except FileNotFoundError:
            self.__cache = {'id':0}
            self.__dump()

    def __dump(self):
        pickle.dump(self.__cache, open(self.__datasource, 'wb'))

    def __load(self):
        self.__cache = pickle.load(open(self.__datasource, 'rb'))

    def add(self, key, obj):
        self.__cache[key] = obj
        self.__cache['id'] += 1
        self.__dump()

    def update(self, key, obj):
        self.__cache[key] = obj
        self.__dump()
    
    def get(self, key):
        try:
            return self.__cache[key]
        except KeyError as e:
            print("Key not found in CACHE")

    def remove(self, key):
        try:
            self.__cache.pop(key)
            self.__dump()
        except KeyError:
            pass

    def get_all(self):
        return [v for k, v in self.__cache.items() if k != "id"]