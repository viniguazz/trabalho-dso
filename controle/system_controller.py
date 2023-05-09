from system_view import SystemView
from game_list_controller import GameListController
from bet_controller import BetController
from user_controller import UserController
from general_register_controller import GeneralRegisterController

class SystemController:

    def __init__(self):
        self.__system_view = SystemView(self)
        self.__game_list_controller = GameListController(self)
        self.__bet_controller = BetController(self)
        self.__user_controller = UserController(self)
        self.__general_register_controller = GeneralRegisterController(self)

    def initialize_system(self):
        self.display_screen()
    
    def list_games(self):
        self.__game_list_controller.display_screen()

    def place_bet(self):
        self.__bet_controller.display_screen()

    def user_status(self):
        self.__user_controller.display_screen()

    def register(self):
        self.__general_register_controller.display_screen()

    def kill_system(self):
        exit(0)

    def display_screen(self):
        option_list = {1: self.list_games, 2: self.place_bet, 3: self.user_status,
                        0: self.kill_system}

        while True:
            option = self.__system_view.display_options()
            selected_function = option_list[option]
            selected_function()