from better_view import BetterView
from better import Better

class BetterControler():
    def __init__(self, system_controller):
        betters = []
        self.__system_controller = system_controller
        self.__better_view = BetterView()
    
    def backtrack(self):
        self.__system_controller.display_screen
    
    def check_better(self):
        better_id = self.__better_view.get_better()
        for better in betters:
            if better_id == better["id"]:
                self.__better_view.display_better_data(better)
            else:
                print('Invalid user!')

    def display_screen(self):
        option_list = {1: self.check_better, 2: self.backtrack}

        while True:
            option = self.__better_view.display_options()
            selected_function = option_list[option]
            selected_function()