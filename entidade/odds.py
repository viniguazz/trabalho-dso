#Luan

import Player from player

class Odds():
    def __init__(self, player1 : Player, 
                player2 : Player, 
                bet_vict_player1 : float, 
                bet_vict_player2 : float):
        if not (isinstance( player1, Player)):
            raise
        if not (isinstance( player2, Player)):
            raise
        self.__player1 = player1.stats()
        self.__player2 = player2.stats()
        self.__odd_vict1 = float()
        self.__odd_vict2 = float()
        self.__odd_draw = float()
    
    @property
    def player1(self):
        return self.__player1
    
    @property
    def player2(self):
        return self.__player2
    
    