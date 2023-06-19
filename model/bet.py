from model import Game, Result, Better
from exception import InvalidNativeTypeException, InvalidGameException, InvalidBetterException, InvalidResultException


class Bet():

    def __init__(self, id: int, price: float, game: Game, better: Better, result: Result, odd : int):

        if not isinstance(price, float):
            raise InvalidNativeTypeException(price, "float")
        if not isinstance(game, Game):
            raise InvalidGameException(game)
        if not isinstance(better, Better):
            raise InvalidBetterException(better)
        if not isinstance(result, Result):
            raise InvalidResultException(result)
        if not isinstance(odd, int):
            raise InvalidNativeTypeException(odd, "int")

        self.__better = better
        self.__game = game
        self.__result = result
        self.__price = price
        self.__id = id
        self.__status = True
        self.__odd = odd

    @property
    def odd(self):
        return self.__odd

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

    @status.setter
    def status(self, status):
        if not isinstance(status, bool):
            raise TipoErradoException
        self.__status = status

    @price.setter
    def price(self, price):
        if not isinstance(price, int):
            raise TipoErradoException
        self.__price = price

    @game.setter
    def game(self, game):
        if not isinstance(game, Game):
            raise TipoErradoException
        self.__game = game

    @better.setter
    def better(self, better):
        if not isinstance(better, Better):
            raise TipoErradoException
        self.__better = better

    @result.setter
    def result(self, result):
        if not isinstance(result, Result):
            raise TipoErradoException
        self.__result = result

    @odd.setter
    def odd(self, odd):
        self.__odd = odd

