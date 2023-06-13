from dao import DAO
from model.better import Better


class BetterDAO(DAO):

    def __init__(self):
        super().__init__('betters.pkl')
    
    def add(self, better: Better):
        if (isinstance(better, Better)) and (isinstance(better.id, int)):
            super().add(better.id, better)

    def get(self, key: int):
        return super().get(key)

    def update(self, better: Better):
        self.remove(better.id)
        self.add(better)
        return super().get(better.id)
    
    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)