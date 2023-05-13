#Luan

#

from player import Player

class Odds():
    def __init__(self, player1 : Player, 
                player2 : Player, 
                bet_vict_player1 : float, 
                bet_vict_player2 : float,
                bet_draw: float):
        if not (isinstance( player1, Player)):
            raise
        if not (isinstance( player2, Player)):
            raise
        if not (isinstance(bet_vict_player1, float)):
            raise
        if not (isinstance(bet_vict_player2, float)):
            raise
        if not (isinstance(bet_draw, float)):
            raise
            
        self.__player1 = player1
        self.__player2 = player2
        self.__bet_vict_player1 = bet_vict_player1
        self.__bet_vict_player2 = bet_vict_player2
        self.__bet_draw = bet_draw
        self.__odd_vict1 = float()
        self.__odd_vict2 = float()
        self.__odd_draw = float()
    
    @property
    def player1(self):
        return self.__player1
    
    @property
    def bet_draw(self):
        return self.__bet_draw
    
    @property
    def player2(self):
        return self.__player2
    
    @property
    def bet_vict_player1(self):
        return self.__bet_vict_player1
    
    @property
    def bet_vict_player2(self):
        return self.__bet_vict_player2

    @player1.setter
    def player1(self, player1):
        self.__player1 = player1
    
    @player2.setter
    def player2(self, player2):
        self.__player2 = player2

    @bet_vict_player1.setter
    def bet_vict_player1(self, bet_vict_player1):
        self.__bet_vict_player1 = bet_vict_player1
    
    @bet_vict_player2.setter
    def bet_vict_player2(self, bet_vict_player2):
        self.__bet_vict_player2 = bet_vict_player2

    @bet_draw.setter
    def bet_draw(self, bet_draw):
        self.__bet_draw = bet_draw

    def calcular_odds(self):
        total = self.__bet_draw + self.__bet_vict_player1 + self.__bet_vict_player2
        odd_vict1 = self.__bet_vict_player1/total
        odd_vict2 = self.__bet_vict_player2/total
        odd_draw = self.__bet_draw/total
        self.__odd_draw = (1/odd_draw) - 1
        self.__odd_vict1 = (1/odd_vict1) - 1 
        self.__odd_vict2 = (1/odd_vict2) - 1