# vini

from model.person import Person
from model.stats import Stats
from exception.tipo_errado_exception import TipoErradoException

# O Player tem um atributo stats em formato de lista. Não precisamos mais de um dicionário, porque só há um esporte.


class Player(Person):

    def __init__(self, id : int, name : str, stats : Stats):
        super().__init__(name)
        if not isinstance(stats, Stats):
            raise TipoErradoException
        self.__stats = stats
        self.__id = id
    
    @property
    def stats(self):
        return self.__stats

    @stats.setter
    def stats(self, stats):
        if not isinstance(stats, Stats):
            raise TipoErradoException
        self.__stats = Stats

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        if not isinstance(id, int):
            raise TipoErradoException
        self.__id = id
    
    
    def change_stats(self, outcome : str):
        if outcome == 'victory':
            self.__stats.add_victory()
        elif outcome == 'loss':
            self.__stats.add_loss()
        else:
            self.__stats.add_draw()