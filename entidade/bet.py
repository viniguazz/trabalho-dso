# vini
from result import Result

# {Luan falando} Precisa implementar um float chamado Odd que puxa o Odd do
# game quando instanciado

class Bet():

    id = 0

    def __init__(self, price : float, game : Game, better: Better, result: Result):
        

        if isinstance(price, float):
            self.__price = price
        if isinstance(game, Game):
            self.__game = game
        if isinstance(better, Better):
            self.__better = better
        if isinstance(result, Result):
            self.__result = result
        self.__id = id
        id += 1
        self.__status = True


    @property
    def id(self):
        return self.__id
    @property
    def status(self):
        return self.__status
    @property
    def price(self):
        return self.__price
    @property
    def game(self):
        return self.__game
    @property
    def better(self):
        return self.__better
    @property
    def result(self):
        return self.__result

    @id.setter
    def id(self, id):
        if isinstance(id, int):
            self.__id = id
    @status.setter
    def status(self, status):
        if isinstance(status, bool):
            self.__status = status
    @price.setter
    def price(self, price):
        if isinstance(price, int):
            self.__price = price
    @game.setter
    def game(self, game):
        if isinstance(game, Game):
            self.__game = game
    @better.setter
    def better(self, better):
        if isinstance(better, Better):
            self.__better = better
    @result.setter
    def result(self, return):
        if isinstance(result, Return):
            self.__result = result