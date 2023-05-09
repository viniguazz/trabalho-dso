from bet_view import BetView
from bet import Bet

class BetController():
    def __init__(self, system_controller):
        bets = []
        currentId = 0
        self.__system_controller = system_controller
        self.__bet_view = bet_view
    
    def get_bet_by_id(self, id : int):
        for bet in bets:
            if bet.id == id:
                return bet
        return None
    
    def add_bet(self):
