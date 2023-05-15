from view.bet_view import BetView
from model.bet import Bet
from time import sleep
from model.result import Result

class BetController():
    def __init__(self, system_controller):
        self.__system_controller = system_controller
        self.__bet_view = BetView()
        self.__bets = []
        self.__id = 0

    def list_bets(self):
        for bet in self.__bets:
            self.__bet_view.display_message(f'id: {bet.id}, name: {bet.name}, result: {bet.result}')
        if len(self.__bets) == 0:
            self.__bet_view.display_message("No bets Found")
        input(self.__bet_view.display_message('Press any key to return...'))

    def add_bet(self):
        bet_data = self.__bet_view.get_bet_info()
        player = None
        for game in self.__system_controller.game_controller.games:
            if  game.id == bet_data["game_id"]:
                for better in self.__system_controller.better_controller.betters:
                    if better.id == bet_data["better_id"]:
                        game = self.__system_controller.game_controller.get_by_id(bet_data["game_id"])
                        better = self.__system_controller.better_controller.get_better_by_id(bet_data["better_id"])
                        if  bet_data["result"]["player"] == 'player1':
                            player = game.player1
                        elif bet_data["result"]["player"] == 'player2':
                            player = game.player2               
                        bet = Bet(self.__id, bet_data["price"], game, better, Result(bet_data["result"]["outcome"], player))
                        better.add_bet(bet)
                        game.add_bet(bet)
                        self.__bets.append(bet)
                        self.id_plus()
                        self.__bet_view.display_message("Bet Created!")
                        input()
                    else:
                        self.__bet_view.display_message("Better not found")
                        input()
                        return
            else:
                self.__bet_view.display_message("Game not found")
                input()
                return
            
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
        self.__system_controller.admin_controller.display_screen()

    def backtrack_system(self):
        self.__system_controller.display_screen()


    def list_display(self):
        self.list_bets()
        self.__system_controller.display_screen()

    def display_place_bet(self):
        option = self.__bet_view.display_add_bet()
        if option == 2:
            self.backtrack_system()
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

    def id_plus(self):
        self.__id +=1