# Luan

#isTraded foi retirado por não termos mais marketplace
#Como é xadrez 1x1 foi retirado n_contestant por enquanto e sport
#Sentiu-se a necessidade de criar uma classe chamada Result
#Ira analisar se fica melhor implementar o odds como dict ou como uma classe própria
#status começa como verdade para indicar que é um jogo em andamento
#accept_bet foi retirado pois ele estava sendo mapeado para uma feature de usuários premium

#pool foi desmenbrado para os três casos, ou seja, quanto é apostado na vitória do player1
#quanto é apostado no player2 e quanto é apostado no empate

#contestants foi transformado em player1 e player2

from bet import Bet
from player import Player
from odds import Odds

class Game():

    id = 0

    def __init__(self, name : str, player1 : Player, player2 : Player):
        if not isinstance(name, str):
            raise

        if not isinstance(player1 , Player):
            raise

        if not isinstance(player2 , Player):
            raise
        
        self.__id = id
        id += 1
        self.__status = True
        self.__pool_draw = 0.0
        self.__pool_vict1 = 0.0
        self.__pool_vict2 = 0.0
        self.__result = None
        self.__odds = None
        self.__bets = list(Bet)
        self.__name = name

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
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        self.__status = status

    @property
    def result(self):
        return self.__result

    @result.setter
    def result(self, result):
        !!!!
        self.__result = result

    @property
    def odds(self):
        return self.__odds

    @odds.setter
    def odds(self, odds):
        self.__odds = odds

    @property
    def bets(self):
        return self.__bets
