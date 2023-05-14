from view.bet_view import BetView
from model.bet import Bet
from time import sleep
from controller.admin_controller import AdminController

class BetController():
    def __init__(self, system_controller):
        self.__system_controller = system_controller
        self.__bet_view = BetView()
        self.__bets = []
        currentId = 0


    def list_bets(self):
        for bet in self.__bets:
            self.__bet_view.display_message(f'id: {bet.id}, name: {bet.name}, result: {bet.result}')
        input(self.__bet_view.display_message('Press any key to return...'))
    
    def add_bet(self):
        bet_data = self.__bet_view.get_bet_info()
        bet_name = bet_data['name']
        player1 = self.__player_controller.get_player_by_id(bet_data['player1'])
        player2 = self.__player_controller.get_player_by_id(bet_data['player2'])
        new_bet = Bet(id, bet_name, player1, player2)
        self.__bets.append(new_bet)
        print(f'New bet create succesfully! ID:{new_bet.id}')
    
    def read_bet(self):
        bet_id = self.__bet_view.get_bet_by_id()
        for bet in self.__bets:
            if bet['id'] == bet_id:
                self.__bet_view.clear_screen()
                print(f'ID: {bet.id()}')
                print(f'Name: {bet.name()}')
                print(f'Player1: {bet.player1()}')
                print(f'Player2: {bet.player2()}')
                input(self.__bet_view.display_message('Press any key to return'))
                return
        print('bet not found!')
        input(self.__bet_view.display_message('Press any key to return'))
    
    def update_bet(self):
        bet_id = self.__bet_view.get_by_id()
        for bet in self.__bets:
            if bet['id'] == bet_id:
                new_data_bet = self.__bet_view.get_bet_info()
                bet.__id = new_data_bet["id"]
                bet.__name = new_data_bet["name"]
                bet.__player1 = new_data_bet["player1"]
                bet.__player2 = new_data_bet["player2"]
            else:
                self.__bet_view.display_message('bet not found!')

    def delete_bet(self):
        bet_id = self.__bet_view.get_bet_by_id()
        for bet in self.__bets:
            if bet['id'] == bet_id:
                self.__bets.remove(bet)
                input(self.__bet_view.display_message('bet deleted succesfully!'))
                return
        print('bet not found!')
        input(self.__bet_view.display_message('Press any key to return'))

    def backtrack(self):
        self.__admin_controller.display_screen()


    def list_display(self):
        self.list_bets()
        self.__system_controller.display_screen()

    def display_screen(self):
        option_list = {1: self.add_bet, 
        2: self.read_bet, 
        3: self.update_bet, 
        4: self.delete_bet, 
        5: self.list_bets, 
        6: self.backtrack}

        while True:
            option = self.__bet_view.display_options()
            selected_function = option_list[option]
            selected_function()

    
"""     def get_bet_by_id(self, id : int):
        for bet in bets:
            if bet.id == id:
                return bet
        return None

    def backtrack(self):
        self.__system_controller.display_screen
    
    def add_bet(self):
        bet_data = self.__bet_view.place_bet()
        if get_bet_by_id(bet_data["bet_id"]) != None:
            bets.append(Bet(bet_data["price"], bet_data["bet_id"], bet_data["better_id"], Result(bet_data["outcome"], bet_data["player"])))
            print('Bet placed successfuly! Be ready to lose, bitch!')
            sleep(1)
        self.__display_screen()

    def display_screen(self):
        option_list = {1: self.add_bet, 2: self.backtrack}

        while True:
            option = self.__bet_view.display_options()
            selected_function = option_list[option]
            selected_function() """
