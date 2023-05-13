from bet_view import BetView
from bet import Bet
from time import sleep

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

    def backtrack(self):
        self.__system_controller.display_screen
    
    def add_bet(self):
        bet_data = self.__bet_view.place_bet()
        if get_bet_by_id(bet_data["bet_id"]) != None:
            bets.append(Bet(bet_data["price"], bet_data["game_id"], bet_data["better_id"], Result(bet_data["outcome"], bet_data["player"])))
            print('Bet placed successfuly! Be ready to lose, bitch!')
            sleep(1)
        self.__display_screen()

    def display_screen(self):
        option_list = {1: self.add_bet, 2: self.backtrack}

        while True:
            option = self.__bet_view.display_options()
            selected_function = option_list[option]
            selected_function()