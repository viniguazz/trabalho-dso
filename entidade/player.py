# vini

from person import Person
from stats import Stats

# O Player tem um atributo stats em formato de lista. Não precisamos mais de um dicionário, porque só há um esporte.


class Player(Person):
    def __init__(self, stats):
        self.__stats = stats
    
    @property
    def stats(self):
        return self.__stats

    @stats.setter
    def stats(self, stats):
        if isinstance(stats, Stats):
            self.__stats = Stats

