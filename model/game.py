from model import Player, Result
from exception import InvalidNativeTypeException, InvalidPlayerException, ClosedGameException


class Game():

    def __init__(self,id: int, name: str, player1: Player, player2: Player):

        if not isinstance(name, str):
            raise InvalidNativeTypeException(name, "str")

        if not isinstance(player1, Player):
            raise InvalidPlayerException(player1)

        if not isinstance(player2, Player):
            raise InvalidPlayerException(player2)
        
        self.__id = id
        self.__player1 = player1
        self.__player2 = player2
        self.__result = None
        self.__bets = []
        self.__name = name

    @property
    def id(self):
        return self.__id

    @property
    def bets(self):
        return self.__bets

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def player1(self):
        return self.__player1

    @player1.setter
    def player1(self, player1):
        self.__player1 = player1
        
    @property
    def player2(self):
        return self.__player2

    @player2.setter
    def player2(self, player2):
        self.__player2 = player2

    @property
    def result(self):
        return self.__result

    @result.setter
    def result(self, result):
        if not (isinstance(result, Result)):
            raise TipoErradoException
        self.__result = result
        self.end_game()

    def generate_odds(self):
        pass

    def add_bet(self, bet_id, price, better, result, odds):
        from model.better import Better
        from model.bet import Bet
        if self.__result != None:
            raise ClosedGameException(self.__name, self.__id)
        new_bet = Bet(bet_id, price, self, better, result, odds)
        self.__bets.append(new_bet)
        return new_bet
    
    def get_bet_by_id(self, id: int):
        for bet in self.__bets:
            if bet.id == id:
                return bet

    def remove_bet(self, id: int):
        bet = self.get_bet_by_id(id)
        self.__bets.remove(bet)

    def end_game(self):           
        for bet in self.__bets:
            if bet.status == True:
                bet.status = False
                if (bet.result.outcome == self.__result.outcome) and (bet.result.player == self.__result.player):
                    bet.better.add_money((bet.price + bet.price*bet.odd))



