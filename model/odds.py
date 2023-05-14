#Luan

#

from model.player import Player
from model.tipo_errado_exception import TipoErradoException

class Odds():
    def __init__(self, 
                player1 : Player, 
                player2 : Player, 
                bet_vict_player1 : float, 
                bet_vict_player2 : float,
                bet_draw: float
                ):
        if not (isinstance( player1, Player)):
            raise TipoErradoException
        if not (isinstance( player2, Player)):
            raise TipoErradoException
        if not (isinstance(bet_vict_player1, float)):
            raise TipoErradoException
        if not (isinstance(bet_vict_player2, float)):
            raise TipoErradoException
        if not (isinstance(bet_draw, float)):
            raise TipoErradoException
            
        self.__player1 = player1
        self.__player2 = player2
        self.__bet_vict_player1 = bet_vict_player1
        self.__bet_vict_player2 = bet_vict_player2
        self.__bet_draw = bet_draw
        self.__odd_vict1 = 0.0
        self.__odd_vict2 = 0.0
        self.__odd_draw = 0.0
        self.calcular_odds()
    
    @property
    def player1(self):
        return self.__player1
    
    @player1.setter
    def player1(self, player1):
        if not (isinstance(player1, Player)):
            raise TipoErradoException
        self.__player1 = player1
    
    @property
    def player2(self):
        return self.__player2
    
    @player2.setter
    def player2(self, player2):
        if not (isinstance(player2, TipoErradoException)):
            raise TipoErradoException
        self.__player2 = player2
    
    @property
    def bet_draw(self):
        return self.__bet_draw
    
    # @bet_draw.setter
    # def bet_draw(self, bet_draw):
    #     if not (isinstance(bet_draw, float)):
    #         raise TipoErradoException
    #     self.__bet_draw = bet_draw 
    
    @property
    def bet_vict_player1(self):
        return self.__bet_vict_player1
    
    
    # @bet_vict_player1.setter
    # def bet_vict_player1(self, bet_vict_player1):
    #     if not (isinstance(bet_vict_player1, float)):
    #         raise TipoErradoException
    #     self.__bet_vict_player1 = bet_vict_player1
    
    @property
    def bet_vict_player2(self):
        return self.__bet_vict_player2
    
    # @bet_vict_player2.setter
    # def bet_vict_player2(self, bet_vict_player2):
    #     if not (isinstance(bet_vict_player2, float)):
    #         raise TipoErradoException
    #     self.__bet_vict_player2 = bet_vict_player2
    
    @property
    def odd_vict1(self):
        return self.__odd_vict1
    
    @property
    def odd_vict2(self):
        return self.__odd_vict2
    
    @property
    def odd_draw(self):
        return self.__odd_draw

    def calcular_odds(self):
        total = self.__bet_draw + self.__bet_vict_player1 + self.__bet_vict_player2
        odd_vict1 = self.__bet_vict_player1/total
        odd_vict2 = self.__bet_vict_player2/total
        odd_draw = self.__bet_draw/total
        self.__odd_draw = (1/odd_draw) - 1
        self.__odd_vict1 = (1/odd_vict1) - 1 
        self.__odd_vict2 = (1/odd_vict2) - 1