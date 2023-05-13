#Luan

#outome vai receber uma string informando qual foi o resultado; Vai ser apenas "Draw" ou "Victory"

from player import Player

class Result():
    def __init__(self, outcome : str, player : Player):
        if not isinstance(outome, str):
            raise
        if not isinstance(player, Player):
            raise
        self.__outome = outome
        if player == None and outcome == "Draw":
            self.__player = None
        else:
            self.__player = player
            
        @property
        def outome(self):
            return self.__outome
        
        @outome.setter
        def outome(self, outome):
            if not isinstance(outome, str):
                raise    
            self.__outome = outome
        
        @property
        def player(self):
            return self.__player
        
        @player.setter
        def player(self, player):
            if not isinstance(player, Player):
                raise
            self.__player = player
