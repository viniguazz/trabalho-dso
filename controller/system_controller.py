from view import SystemView
from controller import AdminController, PlayerController, BetterController, GameController, BetController
from exception import NoMenuSelected

class SystemController:

    def __init__(self):
        self.__system_view = SystemView()
        self.__admin_controller = AdminController(self)
        self.__player_controller = PlayerController(self)
        self.__better_controller = BetterController(self)
        self.__game_controller = GameController(self)
        self.__bet_controller = BetController(self)

    @property
    def admin_controller(self):
        return self.__admin_controller
    
    @property
    def better_controller(self):
        return self.__better_controller
    
    @property
    def game_controller(self):
        return self.__game_controller
    
    @property
    def bet_controller(self):
        return self.__bet_controller
    
    @property
    def player_controller(self):
        return self.__player_controller

    def initialize_system(self):
        self.display_screen()
    
    def list_games(self):
        self.__game_controller.list_games()

    def place_bet(self):
        self.__bet_controller.add_bet()

    def better_status(self):
        self.__better_controller.display_balance_and_bets()

    def admin_menu(self):
        self.__admin_controller.display_screen()

    def kill_system(self):
        exit(0)

    def display_screen(self):
        try:
            option_list = {0: self.kill_system,
            1: self.list_games, 
            2: self.place_bet, 
            3: self.better_status, 
            4: self.admin_menu, 
            5: self.kill_system}

            while True:
                option = self.__system_view.display_options()
                selected_function = option_list[option]
                selected_function()
        except(NoMenuSelected) as e:
            self.__system_view.display_message(e)
            self.display_screen()