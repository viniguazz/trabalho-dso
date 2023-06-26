from exception import InvalidNativeTypeException


class Result():

    def __init__(self, outcome: str, player: str = None):
        if not isinstance(outcome, str):
            raise InvalidNativeTypeException(outcome, "str")
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
            raise InvalidNativeTypeException(outcome, "str")    
        self.__outcome = outcome
    
    @property
    def player(self):
        return self.__player
    
    @player.setter
    def player(self, player):
        if not isinstance(player, str):
            raise InvalidNativeTypeException(player, "str")
        self.__player = player
