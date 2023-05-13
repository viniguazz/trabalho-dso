#Luan

#outcome vai receber uma string informando qual foi o resultado; Vai ser apenas "Draw" ou "Victory"

from player import Player
from tipo_errado_exception import TipoErradoException

class Result():
    def __init__(self, outcome : str, player : Player = None):
        if not isinstance(outcome, str):
            raise TipoErradoException
        if not (isinstance(player, Player) or None):
            raise TipoErradoException
        self.__outcome = outcome
        if player == None and outcome == "Draw":
            self.__player = None
        else:
            self.__player = player
            
        @property
        def outcome(self):
            return self.__outcome
        
        @outcome.setter
        def outcome(self, outcome):
            if not isinstance(outcome, str):
                raise TipoErradoException    
            self.__outcome = outcome
        
        @property
        def player(self):
            return self.__player
        
        @player.setter
        def player(self, player):
            if not isinstance(player, Player):
                raise TipoErradoException
            self.__player = player
