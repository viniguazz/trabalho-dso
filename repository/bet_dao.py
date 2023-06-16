from dao import DAO
from model.bet import Bet

class BetDAO(DAO):

    def __init__(self):
        super().__init__('bets.pkl')
    
    def add(self, bet: Bet):
        if (isinstance(bet, Bet)) and (isinstance(bet.id, int)):
            super().add(bet.id, bet)

    def get(self, key: int):
        return super().get(key)

    def update(self, bet: Bet):
        self.remove(bet.id)
        self.add(bet)
        return super().get(bet.id)
    
    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)