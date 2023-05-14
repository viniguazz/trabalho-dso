from view.system_view import SystemView
from controller.admin_controller import AdminController
from controller.player_controller import PlayerController
from controller.better_controller import BetterController
from controller.game_controller import GameController
from controller.bet_controller import BetController

class SystemController:

    def __init__(self):
        self.__system_view = SystemView
        self.__admin_controller = AdminController(self)
        self.__player_controller = PlayerController(self)
        self.__better_controller = BetterController(self)
        self.__game_controller = GameController(self)
        self.__bet_controller = BetController(self)

    def initialize_system(self):
        self.display_screen()
    
    def list_games(self):
        self.__game_controller.display_screen()

    def place_bet(self):
        self.__bet_controller.display_screen()

    def better_status(self):
        self.__user_controller.display_screen()

    def admin_menu(self):
        self.__admin_controller.display_screen()

    def kill_system(self):
        exit(0)

    def display_screen(self):
        option_list = {1: self.list_games, 
        2: self.place_bet, 
        3: self.better_status, 
        4: self.admin_menu, 
        5: self.kill_system}

        while True:
            option = self.__system_view.display_options()
            selected_function = option_list[option]
            selected_function()