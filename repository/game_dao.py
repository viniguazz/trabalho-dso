from repository.dao import DAO
from model.game import Game


class GameDAO(DAO):

    def __init__(self):
        super().__init__('games.pkl')
    
    def add(self, game: Game):
        if (isinstance(game, Game)) and (isinstance(game.id, int)):
            super().add(game.id, game)

    def get(self, key: int):
        return super().get(key)

    def update(self, game: Game):
        self.remove(game.id)
        self.add(game)
        return super().get(game.id)
    
    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)