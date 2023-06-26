import os
from view import AdminView
from exception import NoMenuSelected


class AdminController():
    
    def __init__(self, system_controller):
        self.__system_controller = system_controller
        self.__admin_view = AdminView()
        self.__password = 'rickastley'
        self.__god_mode_enabled = True
    
    def crud_players(self):
        self.__system_controller.player_controller.display_screen()
    def crud_betters(self):
        self.__system_controller.better_controller.display_screen()
    def crud_games(self):
        self.__system_controller.game_controller.display_screen()
    def crud_bets(self):
        self.__system_controller.bet_controller.display_screen()
    def backtrack(self):
        self.__system_controller.display_screen()

    def display_screen(self):
        option_list = {0:self.backtrack,
        1: self.crud_games, 
        2: self.crud_players, 
        3: self.crud_betters, 
        4: self.crud_bets, 
        5: self.backtrack}
        
        if (not self.__god_mode_enabled):
            if (self.__admin_view.login() == self.__password):
                self.__god_mode_enabled = True
                self.__admin_view.display_message('GOD MODE ENABLED!')
            else:
                self.__admin_view.display_message('Wrong password! PRO TIP: He\'ll never give you up...')
                self.__admin_view.close()
                self.backtrack()
        
        while True:
            option = self.__admin_view.display_options()
            selected_function = option_list[option]
            selected_function()
   
