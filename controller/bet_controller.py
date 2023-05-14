from view.bet_view import BetView
from model.bet import Bet
from time import sleep
from model.result import Result

class BetController():
    def __init__(self, system_controller):
        self.__system_controller = system_controller
        self.__bet_view = BetView()
        self.__bets = []

    def list_bets(self):
        for bet in self.__bets:
            self.__bet_view.display_message(f'id: {bet.id}, name: {bet.name}, result: {bet.result}')
        input(self.__bet_view.display_message('Press any key to return...'))

    def add_bet(self):
        bet_data = self.__bet_view.get_bet_info()
        for game in self.__system_controller.game_controller.games:
            if not game.id == bet_data["game_id"]:
                self.__bet_view.display_message('Game not found') 
                return 
        for better in self.__system_controller.better_controller.betters:
            if not better.cpf == bet_data["cpf"]:
                self.__bet_view.display_message("Better not found")
                return
        
        #Olhar o get_by_cpf depois
        game = self.__system_controller.game_controller.get_by_id(bet_data["game_id"])
        better = self.__system_controller.better_controller.get_by_cpf(bet_data["cpf"])
        bet = Bet(bet_data["price"], game, better, Result(bet_data["result"]["outcome"], bet_data["result"]["player"]))
        better.add_bet(bet)
        game.add_bet(bet)
        self.__bets.append(bet)

    def read_bet(self):
        bet_id = self.__bet_view.get_by_id()
        for bet in self.__bets:
            if bet['id'] == bet_id:
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
        for bet in self.__bets:
            if bet['id'] == bet_id:
                for game in self.__system_controller.game_controller.games:
                    if game.bet['id'] == bet['id']:
                        game.remove_bet(bet)
                        bet.better.remove_bet(bet)
                        self.__bets.remove(bet)
                        self.__bet_view.display_message("Bet Deleted!")
                        input('Press any key to return')
                        return
        self.__bet_view.display_message('bet not found!')
        input('Press any key to return')
        return

    def backtrack(self):
        self.__admin_controller.display_screen()


    def list_display(self):
        self.list_bets()
        self.__system_controller.display_screen()

    def display_place_bet(self):
        option = self.__bet_view.display_add_bet()
        if option == 2:
            self.backtrack()
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

    def backtrack(self):
        self.__system_controller.display_screen()