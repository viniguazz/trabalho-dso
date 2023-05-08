# vini

class Stats():
    def __init__(self, victories : int, losses : int, draws : int):
        if isinstance(victories, int):
            self.__victories = victories
        if isinstance(losses, int):
            self.__losses = losses
        if isinstance(draws, int):
            self.__draws = draws


    @property
    def victories(self):
        return self.__victories
    @property
    def losses(self):
        return self.__losses
    @property
    def draws(self):
        return self.__draws


    def add_victory(self):
        self.__victories += 1

    def add_loss(self):
        self.__losses += 1

    def add_draw(self):
        self.__draw += 1