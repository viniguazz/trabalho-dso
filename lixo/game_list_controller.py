from game_list_view import GameListView
from game import Game

class GameListController():
    def __init__(self, system_controller):
        self.__system_controller = system_controller
        self.__game_controller = game_controller
        self.__game_list_view = GameListView()
    
    def backtrack(self):
        self.__system_controller.display_screen

    def get_game_by_id(self, id : int):
        for game in games:
            if game.id == id:
                return game
        return None
    
    def list_games(self):
        for game in self.__game_controller.games:
            self.__game_list_view.display_game(game)
        input('Press any key to exit list')
        backtrack()


    
    

