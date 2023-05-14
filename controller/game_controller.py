from view.game_view import GameView
from model.game import Game
from controller.player_controller import PlayerController

class GameController():

    def __init__(self, system_controller):
        self.__system_controller = system_controller
        #????
        # self.__admin_controller = admin_controller
        self.__player_controller = PlayerController
        #????
        self.__game_view = GameView()
        self.__games = []

    def list_games(self):
        for game in self.__games:
            self.__game_view.display_message(f'id: {game["id"]}, name: {game["name"]}, result: {game["result"]}')
        self.__game_view.display_message('Press any key to return...')
    
    def add_game(self):
        game_data = self.__game_view.get_game_info()
        game_name = game_data['name']
        player1 = self.__player_controller.get_player_by_id(game_data['player1'])
        player2 = self.__player_controller.get_player_by_id(game_data['player2'])
        new_game = Game(id, game_name, player1, player2)
        if new_game not in self.__games:
            self.__games.append(new_game)           
        self.__game_view.display_message(f'New game create succesfully! ID:{new_game.id}')
    
    def read_game(self):
        game_id = self.__game_view.get_by_id()
        for game in self.__games:
            if game['id'] == game_id:
                self.__game_view.clear_screen()
                print(f'ID: {game.id()}')
                print(f'Name: {game.name()}')
                print(f'Player1: {game.player1()}')
                print(f'Player2: {game.player2()}')
                input(self.__game_view.display_message('Press any key to return...'))
                return
        self.__game_view.display_message('Game not found!')
        input(self.__game_view.display_message('Press any key to return...'))
    
    def update_game(self):
        game_id = self.__game_view.get_by_id()
        for game in self.__games:
            if game['id'] == game_id:
                new_data_game = self.__game_view.get_game_info()
                game.__id = new_data_game["id"]
                game.__name = new_data_game["name"]
                game.__player1 = new_data_game["player1"]
                game.__player2 = new_data_game["player2"]
            else:
                self.__game_view.display_message('Game not found!')

    def delete_game(self):
        game_id = self.__game_view.get_by_id()
        for game in self.__games:
            if game['id'] == game_id:
                self.__games.remove(game)
                input(self.__game_view.display_message('Game deleted succesfully!'))
                return
        self.__game_view.display_message('Game not found!')
        input(self.__game_view.display_message('Press any key to return'))

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

    def get_by_id(self, id):
        for game in self.__games:
            if game.id == id:
                return game
        self.__game_view.display_message("Game not Found")
        return None