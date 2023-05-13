from better_view import BetterView
from better import Better

class BetterControler():
    def __init__(self, system_controller):
        self.__betters = []
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

    def get_better_by_id(self, id):
        for better in self.__betters:
            if id == better.id:
                return better
        print('Invalid player!')
        return None
    
    def list_betters(self):
        for better in self.__betters:
            print('===========================================')
            self.__better_view.display_message(f'ID: {better.id}, 
            Nick: {better.nick}, 
            CPF: {better.cpf},
            Funds: {better.wallet}')
            print('===========================================')
        input('Press any key to return...')
    
    def add_better(self):
        better_data = get_better_info()
        better_name = better_data['name']
        better_nick = better_data['nick']
        better_cpf = better_data['cpf']
        better_funds = better_data['wallet']
        new_better = Better(better_name, better_nick, better_funds, better_cpf)
        unique = True
        for better in self.__betters:
            if better.cpf == better_cpf:
                unique = False
        if unique:
            self.__betters.append(new_player)
            print(f'New better create succesfully! ID:{new_better.id}')
        else:
            print('Better already in the database! Process failed!')
    
    def read_better(self):
        better_id = self.__better_view.get_by_id()
        for better in self.__betters:
            if better['id'] == better_id:
                os.system('cls')
                print(f'ID: {better['id']}')
                print(f'Name: {better['name']}')
                print(f'Nick: {better['nick']}')
                print(f'CPF: {better['cpf']}')
                print(f'Funds: {better['wallet']}')
                input('Press any key to return')
                return
        print('Better not found!')
        input('Press any key to return')
    
    #incompleto assim como o de game
    def update_better(self):
        player_id = self.__game_view.get_bet_by_id()
        for game in self.__games:
            if game['id'] == game_id:

    def delete_better(self):
        better_id = self.__better_view.get_by_id()
        for better in self.__betters:
            if better['id'] == better_id:
                self.__betters.remove(better)
                input('Better deleted succesfully!')
                return
        print('Better not found!')
        input('Press any key to return')

    def backtrack(self):
        self.__admin_controller.display_screen()

    def display_screen(self):
        option_list = {1: self.add_better, 
        2: self.read_better, 
        3: self.update_better, 
        4: self.delete_better, 
        5: self.list_better, 
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