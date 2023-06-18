from view.bet_view import BetView
from model.bet import Bet
from time import sleep
from model.result import Result
from model.player import Player
from repository.bet_dao import BetDAO

class BetController():
    def __init__(self, system_controller):
        self.__system_controller = system_controller
        self.__bet_view = BetView()
        self.__bet_dao = BetDAO()

    def list_bets(self):
        for bet in self.__bet_dao.get_all():
            if not bet.result.outcome == 'Draw':
                self.__bet_view.display_message(f'id: {bet.id}, game: {bet.game.name}, Outcome: {bet.result.outcome}, Player: {bet.result.player.name}')
            else:
                self.__bet_view.display_message(f'id: {bet.id}, game: {bet.game.name}, Outcome: {bet.result.outcome}')
        if len(self.__bet_dao.get_all()) == 0:
            self.__bet_view.display_message("No bets Found")
        input(self.__bet_view.display_message('Press any key to return...'))

    def add_bet(self):
        bet_data = self.__bet_view.get_bet_info()
        bet_game = self.__system_controller.game_controller.get_by_id(int(bet_data["game_id"]))
        bet_price = bet_data["price"]
        bet_better = self.__system_controller.better_controller.get_better_by_id(bet_data["better_id"])
        try:
            bet_better.remove_money(bet_price)
            bet_result = Result(bet_data["result"]["outcome"], player)
            bet_odds = bet_data['odd']
            bet_id = self.__bet_dao.get_current_id() + 1
            new_bet = bet.game.add_bet(bet_id, bet_price, bet_better, bet_result, bet_odds)
            self.__bet_dao.add(new_bet)
            self.___system_controller.game_controller.save_game(bet_game)
        except AttributeError:
            return

    def read_bet(self):
        bet_id = self.__bet_view.get_by_id()
        for bet in self.__bet_dao.get_all():
            if bet.id == bet_id:
                self.__bet_view.clear_screen()
                self.__bet_view.display_message(f'ID: {bet.id()}')
                self.__bet_view.display_message(f'Name: {bet.name()}')
                self.__bet_view.display_message(f'Player1: {bet.player1()}')
                self.__bet_view.display_message(f'Player2: {bet.player2()}')
                input('Press any key to return')
                return
        print('bet not found!')
        input('Press any key to return')
    
    def delete_bet(self):
        bet_id = self.__bet_view.get_by_id()
        for bet in self.__bet_dao.get_all():
            if bet.id == bet_id:
                bet.game.remove_bet(bet.id)
                self.___system_controller.game_controller.save_game(bet.game)
                self.__bet_dao.remove(bet.id)
                self.__bet_view.display_message("Bet Deleted!")
                input('Press any key to return')
                return
        self.__bet_view.display_message('bet not found!')
        input('Press any key to return')
        return
    
    def delete_bet_by_id(self, id):
        bet_id = id
        for bet in self.__bet_dao.get_all():
            if bet.id == id:
                bet.game.remove_bet(bet.id)
                self.___system_controller.game_controller.save_game(bet.game)
                self.__bet_dao.remove(bet.id)
                self.__bet_view.display_message("Bet Deleted!")
                input('Press any key to return')
                return
        self.__bet_view.display_message('bet not found!')
        input('Press any key to return')
        return

    def backtrack(self):
        self.__system_controller.admin_controller.display_screen()

    def list_display(self):
        self.list_bets()
        self.__system_controller.display_screen()

    def display_place_bet(self):
        option = self.__bet_view.display_add_bet()
        if option == 2:
            self.__system_controller.display_screen()
        elif option == 1:
            self.add_bet()

    def display_screen(self):
        option_list = {1: self.add_bet, 
        2: self.read_bet, 
        3: self.delete_bet, 
        4: self.list_bets, 
        5: self.backtrack}

        while True:
            option = self.__bet_view.display_options()
            selected_function = option_list[option]
            selected_function()

