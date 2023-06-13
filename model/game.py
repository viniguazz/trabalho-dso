from model.player import Player
from model.result import Result
from exception.tipo_errado_exception import TipoErradoException

class Game():
    def __init__(self,id : int, name : str, player1 : Player, player2 : Player):

        if not isinstance(name, str):
            raise TipoErradoException

        if not isinstance(player1 , Player):
            raise TipoErradoException

        if not isinstance(player2 , Player):
            raise TipoErradoException
        
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
        self.encerrar_jogo()
        
    def add_bet(self, bet):
        from model.bet import Bet
        if not (isinstance(bet, Bet)):
            raise TipoErradoException
        self.__bets.append(bet)

    def remove_bet(self,bet):
        from model.bet import Bet
        if not (isinstance(bet,Bet)):
            raise TipoErradoException
        self.__bets.remove(bet)

    def encerrar_jogo(self):             
        for bet in self.__bets:
            if bet.status == True:
                bet.status = False
                if (bet.result.outcome == self.__result.outcome) and (bet.result.player == self.__result.player):
                    bet.better.add_money((bet.price + bet.price*bet.odd))
