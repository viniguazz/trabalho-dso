from dao import DAO


class PlayerDao(DAO):
    
    def __init__(self):
        super().__init__('players.pkl')
    
    def add(self, player: Player):
        if (isinstance(player, Player)) and (isinstance(player.id, int)):
            super().add(player.id, player)

    def get(self, key: int):
        return super().get(key)

    def update(self, player: Player, key: int):
        self.remove(key)
        self.add(player)
        return super().get(key)
    
    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)


    
