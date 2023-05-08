# vini

class Bet():
    def __init__(self, id: int, status : bool, price : float, game : Game, better: Better, result: str):
        if isinstance(id, int):
            self.__id = id
        if isinstance(status, bool):
            self.__status = status
        if isinstance(price, float):
            self.__price = price
        if isinstance(game, Game):
            self.__game = game
        if isinstance(better, Better):
            self.__better = better
        if isinstance(result, str):
            self.__result = result
    
    @property
    def id(self):
        return self.__id
    @property
    def status(self):
        return self.__status
    @property
    def price(self):
        return self.__price