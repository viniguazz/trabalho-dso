from view.bet_view import BetView
from model.bet import Bet
from time import sleep
from model.result import Result
from model.player import Player
from repository.bet_dao import BetDAO
import inspect

class BetController():
    def __init__(self, system_controller):
        self.__system_controller = system_controller
        self.__bet_view = BetView()
        self.__bet_dao = BetDAO()
        if len(list(self.__bet_dao.get_all())) == 0:
            self.__id = 0
        else:
            self.__id = list(self.__bet_dao.get_all())[-1].id + 1

    def id_plus(self):
        self.__id +=1

    def list_bets(self):
        print(self.__bet_dao.get_all())
        self.__bet_view.list_bets(self.__bet_dao.get_all())

    def add_bet(self):
        caller_frame = inspect.currentframe().f_back
        caller_name = inspect.getframeinfo(caller_frame).function
        bet_data = self.__bet_view.get_bet_info()
        if bet_data == None:
            self.__bet_view.close()
            if caller_name == self.display_screen:
                self.backtrack()
            else:
                self.backtrack_system                        
            return
        player = None
        for game in self.__system_controller.game_controller.games:
            if game.result == None:
                if  game.id == bet_data["game_id"]:
                    for better in self.__system_controller.better_controller.betters:
                        if better.id == bet_data["better_id"]:
                            game = self.__system_controller.game_controller.get_by_id(bet_data["game_id"])
                            better = self.__system_controller.better_controller.get_better_by_id(bet_data["better_id"])
                            better.remove_money(bet_data["price"])
                            if  bet_data["result"]["player"] == 'player1':
                                player = game.player1
                            elif bet_data["result"]["player"] == 'player2':
                                player = game.player2               
                            bet = Bet(self.__id, bet_data["price"], game, better, Result(bet_data["result"]["outcome"], player), bet_data['odd'])
                            better.add_bet(bet)
                            game.add_bet(bet)
                            self.__bet_dao.add(bet)
                            self.__system_controller.better_controller.bet_dao.add(bet)
                            self.__system_controller.game.bet_dao.add(bet)
                            self.id_plus()
                            self.__bet_view.display_message("Bet Created!")
                            if caller_name == self.display_screen:
                                self.backtrack()
                            else:
                                self.backtrack_system
                            return
                    else:
                        self.__bet_view.display_message("Better not found")
                        if caller_name == self.display_screen:
                            self.backtrack()
                        else:
                            self.backtrack_system                        
                        return
            else:
                self.__bet_view.display_message("Game already ended!")
                if caller_name == self.display_screen:
                    self.backtrack()
                else:
                    self.backtrack_system
                return
        else:
            self.__bet_view.display_message("Game not found")
            if caller_name == self.display_screen:
                self.backtrack()
            else:
                self.backtrack_system            
            return

    def read_bet(self):
        bet_id = self.__bet_view.get_by_id()
        for bet in self.__bet_dao.get_all():
            if bet.id == bet_id:
                message = f'ID: {bet.id}\nGame: {bet.game.name}\nPrice: {bet.price}\nOutcome: {bet.result.outcome}\nPlayer: {bet.result.player}\nOdd: {bet.odd}'
                self.__bet_view.display_message(message)
                return
        self.__bet_view.display_message('bet not found!')
    

    def delete_bet(self):
        bet_id = self.__bet_view.get_by_id()
        for bet in self.__bet_dao.get_all():
            if bet.id == bet_id:
                for game in self.__system_controller.game_controller.games:
                    for game_bet in game.bets:
                        if game_bet.id == bet.id:
                            game.remove_bet(bet)
                            bet.better.remove_bet(bet)
                            self.__bet_dao.remove(bet.id)
                            self.__bet_view.display_message("Bet Deleted!")
                            return
        self.__bet_view.display_message('bet not found!')
        return
    
    def delete_bet_by_id(self, id):
        for bet in self.__bet_dao.get_all():
            if bet.id == id:
                for game in self.__system_controller.game_controller.games:
                    for game_bet in game.bets:
                        if game_bet.id == bet.id:
                            game.remove_bet(bet)
                            bet.better.remove_bet(bet)
                            self.__bet_dao.remove(bet.id)
                            self.__bet_view.display_message("Bet Deleted!")
                            return
        self.__bet_view.display_message('bet not found!')
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
        self.backtrack_system()

    def display_screen(self):
        option_list = {0: self.backtrack,
        1: self.add_bet, 
        2: self.read_bet, 
        3: self.delete_bet, 
        4: self.list_bets, 
        5: self.backtrack}

        while True:
            option = self.__bet_view.display_options()
            selected_function = option_list[option]
            selected_function()

