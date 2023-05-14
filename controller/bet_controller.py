from view.bet_view import BetView
from model.bet import Bet
from time import sleep

class BetController():
    def __init__(self, system_controller):
        bets = []
        currentId = 0
        self.__system_controller = system_controller
        self.__bet_view = bet_view()
    
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
            bets.append(Bet(bet_data["price"], bet_data["game_id"], bet_data["better_id"], Result(bet_data["outcome"], bet_data["player"])))
            print('Bet placed successfuly! Be ready to lose, bitch!')
            sleep(1)
        self.__display_screen()

    def display_screen(self):
        option_list = {1: self.add_bet, 2: self.backtrack}

        while True:
            option = self.__bet_view.display_options()
            selected_function = option_list[option]
            selected_function() """





from game_view import GameView
from game import Game

class GameController():

    def __init__(self, admin_controller, player_controller, system_controller):
        self.__system_controller = system_controller
        self.__admin_controller = admin_controller
        self.__player_controller = player_controller
        self.__game_view = GameView()
        self.__games = []

    def list_games(self):
        for game in self.__games:
            self.__game_view.display_message(f'id: {game.id}, name: {game.name}, result: {game.result}')
        input('Press any key to return...')
    
    def add_game(self):
        game_data = get_game_info()
        game_name = game_data['name']
        player1 = self.__player_controller.get_player_by_id(game_data['player1'])
        player2 = self.__player_controller.get_player_by_id(game_data['player2'])
        new_game = Game(id, game_name, player1, player2)
        games.append(new_game)
        print(f'New game create succesfully! ID:{new_game.id}')
    
    def read_game(self):
        game_id = self.__game_view.get_bet_by_id()
        for game in self.__games:
            if game['id'] == game_id:
                os.system('cls')
                print(f'ID: {game['id']}')
                print(f'Name: {game['name']}')
                print(f'Player1: {game['player1']}')
                print(f'Player2: {game['player2']}')
                input('Press any key to return')
                return
        print('Game not found!')
        input('Press any key to return')
    
    def update_game(self):
        game_id = self.__game_view.get_bet_by_id()
        for game in self.__games:
            if game['id'] == game_id:

    def delete_game(self):
        game_id = self.__game_view.get_bet_by_id()
        for game in self.__games:
            if game['id'] == game_id:
                self.__games.remove(game)
                input('Game deleted succesfully!')
                return
        print('Game not found!')
        input('Press any key to return')

    def backtrack(self):
        self.__admin_controller.display_screen()


    def list_display(self):
        self.list_games()
        self.__system_controller.display_screen()

    def display_screen(self):
        option_list = {1: self.add_game, 
        2: self.read_game, 
        3: self.update_game, 
        4: self.delete_game, 
        5: self.list_games, 
        6: self.backtrack}

        while True:
            option = self.__game_view.display_options()
            selected_function = option_list[option]
            selected_function()
