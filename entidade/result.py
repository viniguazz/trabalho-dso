#Luan

#win declara se houve vitória ou foi um empate, em caso de vitória também há a necessidade
#de declarar o vencedor

from player import Player

class Result():
    def __init__(self, win : bool, player : Player):
        if not isinstance(win, bool):
            raise
        if not isinstance(player, Player):
            raise
        self.__win = win
        if player == None:
            self.__player = None
        else:
            self.__player = player
            
        @property
        def win(self):
            return self.__win
        
        @win.setter
        def win(self, win):
            if not isinstance(win, bool):
                raise    
            self.__win = win
        
        @property
        def player(self):
            return self.__player
        
        @player.setter
        def player(self, player):
            if not isinstance(player, Player):
                raise
            self.__player = player
