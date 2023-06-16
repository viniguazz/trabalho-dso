from repository.dao import DAO
from model.player import Player


class PlayerDAO(DAO):
    
    def __init__(self):
        super().__init__('players.pkl')
    
    def add(self, player: Player):
        if (isinstance(player, Player)) and (isinstance(player.id, int)):
            super().add(player.id, player)

    def get(self, key: int):
        return super().get(key)

    def update(self, player: Player):
        self.remove(player.id)
        self.add(player)
        return super().get(player.id)
    
    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)


    
