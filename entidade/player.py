# vini

from person import Person
from stats import Stats

# O Player tem um atributo stats em formato de lista. Não precisamos mais de um dicionário, porque só há um esporte.


class Player(Person):
    def __init__(self, stats : Stats):
        self.__stats = stats
    
    @property
    def stats(self):
        return self.__stats

    @stats.setter
    def stats(self, stats):
        if isinstance(stats, Stats):
            self.__stats = Stats
    
    def change_stats(self, outcome : str):
        if outcome == 'victory':
            self.__stats.add_victory()
        elif outcome == 'loss':
            self.__stats.add_loss()
        else:
            self.__stats.add_draw()


