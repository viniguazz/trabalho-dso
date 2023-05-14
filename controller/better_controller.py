from view.better_view import BetterView
from model.better import Better

class BetterController():
    def __init__(self, system_controller):
        self.__betters = []
        self.__system_controller = system_controller
        self.__better_view = BetterView()
    
    def backtrack(self):
        self.__system_controller.display_screen
    
    # def check_better(self):
    #     better_id = self.__better_view.get_better()
    #     for better in self.__betters:
    #         if better_id == better["id"]:
    #             self.__better_view.display_better_data(better)
    #         else:
    #             self.__better_view.display_message('Invalid user!')

    def get_better_by_id(self, id):
        for better in self.__betters:
            if id == better.id:
                return better
        self.__better_view.display_message('Invalid player!')
        return None
    
    def list_betters(self):
        for better in self.__betters:
            self.__better_view.display_message(f'name: {better.name}, nick: {better.nick}, wallet: {better.wallet}, cpf: {better.cpf}')
        self.__better_view.display_message('Press any key to return...')
    
    def add_better(self):
        better_data = BetterView.get_better_info()
        better_name = better_data['name']
        better_nick = better_data['nick']
        better_cpf = better_data['cpf']
        better_funds = better_data['wallet']
        new_better = Better(better_name, better_nick, better_funds, better_cpf)
        if new_better not in self.__betters:
            self.__betters.append(new_better)
            self.__better_view.display_message(f'New better create succesfully! ID:{new_better.id}')
        else:
            self.__better_view.display_message('Better already in the database! Process failed!')
    
    def read_better(self):
        better_id = self.__better_view.get_by_id()
        for better in self.__betters:
            if better['id'] == better_id:
                self.__better_view.clear_screen()
                self.__better_view.display_message(f'ID: {better["id"]}')
                self.__better_view.display_message(f'Name: {better["name"]}')
                self.__better_view.display_message(f'Nick: {better["nick"]}')
                self.__better_view.display_message(f'CPF: {better["cpf"]}')
                self.__better_view.display_message(f'Funds: {better["wallet"]}')
                input(self.__better_view.display_message('Press any key to return'))
                return
        self.__better_view.display_message('Better not found!')
        input(self.__better_view.display_message('Press any key to return'))
    
    def update_better(self):
        better_id = self.__better_view.get_by_id()
        for better in self.__betters:
            if better['id'] == better_id:
                new_data_better = self.__better_view.get_better_info()
                better.__name = new_data_better["name"]
                better.__nick = new_data_better["nick"]
                better.__cpf = new_data_better["cpf"]
                better.__wallet = new_data_better["wallet"]
            else:
                self.__better_view.display_message('better not found!')

    def delete_better(self):
        better_id = self.__better_view.get_by_id()
        for better in self.__betters:
            if better['id'] == better_id:
                self.__betters.remove(better)
                input(self.__better_view.display_message('Better deleted succesfully!'))
                return
        self.__better_view.display_message('Better not found!')
        input(self.__better_view.display_message('Press any key to return'))

    def backtrack(self):
        self.__admin_controller.display_screen()

    def display_screen(self):
        option_list = {1: self.add_better, 
        2: self.read_better, 
        3: self.update_better, 
        4: self.delete_better, 
        5: self.list_betters, 
        6: self.backtrack}

        while True:
            option = self.__better_view.display_options()
            selected_function = option_list[option]
            selected_function()

""" 

    def display_screen(self):
        option_list = {1: self.check_better, 2: self.backtrack}

        while True:
            option = self.__better_view.display_options()
            selected_function = option_list[option]
            selected_function() """