# vini

from model.tipo_errado_exception import TipoErradoException

class Stats():
    def __init__(self, victories : int, losses : int, draws : int):
        if not isinstance(victories, int):
            raise TipoErradoException
        if not isinstance(losses, int):
            raise TipoErradoException
        if not isinstance(draws, int):
            raise TipoErradoException
        self.__losses = losses
        self.__draws = draws
        self.__victories = victories


    @property
    def victories(self):
        return self.__victories
    
    @victories.setter
    def victories(self,victories):
        self.__victories = victories
    
    @property
    def losses(self):
        return self.__losses
    
    @losses.setter
    def losses(self, losses):
        self.__losses = losses
    
    @property
    def draws(self):
        return self.__draws
    
    @draws.setter
    def draws(self, draws):
        self.__draws = draws

    def add_victory(self):
        self.__victories += 1

    def add_loss(self):
        self.__losses += 1

    def add_draw(self):
        self.__draw += 1