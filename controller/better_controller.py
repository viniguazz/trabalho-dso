from view.better_view import BetterView
from model.better import Better
from repository.better_dao import BetterDAO

class BetterController():
    def __init__(self, system_controller):
        self.__system_controller = system_controller
        self.__better_view = BetterView()
        self.__better_dao = BetterDAO()
        if len(list(self.__better_dao.get_all())) == 0:
            self.__id = 0
        else:
            self.__id = list(self.__better_dao.get_all())[-1].id + 1
    
    @property
    def betters(self):
        return self.__better_dao.get_all()

    def id_plus(self):
        self.__id +=1

    def get_better_by_id(self, id):
        for better in self.__better_dao.get_all():
            if id == better.id:
                return better
        self.__better_view.display_message('Invalid Better!')
        return None
    
    def list_betters(self):
        for better in self.__better_dao.get_all():
            self.__better_view.display_message(f'name: {better.name}, nick: {better.nick}, wallet: {better.wallet}, cpf: {better.cpf}')
        if len(self.__better_dao.get_all()) == 0:
            self.__better_view.display_message('No betters found')
        self.__better_view.display_message('Press any key to return...')
        input()
    
    def add_better(self):
        better_data = self.__better_view.get_better_info()
        better_name = better_data['name']
        better_nick = better_data['nick']
        better_cpf = better_data['cpf']
        better_funds = better_data['wallet']
        new_better = Better(self.__id, better_name, better_nick, better_funds, better_cpf)
        self.id_plus()
        if new_better not in self.__better_dao.get_all():
            self.__better_dao.add(new_better)
            self.__better_view.display_message(f'New better create succesfully! ID:{new_better.id}')
            input()
        else:
            self.__better_view.display_message('Better already in the database! Process failed!')
            input()
    
    def read_better(self):
        better_id = self.__better_view.get_by_id()
        for better in self.__better_dao.get_all():
            if better.id == better_id:
                self.__better_view.clear_screen()
                self.__better_view.display_message(f'ID: {better.id}')
                self.__better_view.display_message(f'Name: {better.name}')
                self.__better_view.display_message(f'Nick: {better.nick}')
                self.__better_view.display_message(f'CPF: {better.cpf}')
                self.__better_view.display_message(f'Funds: {better.wallet}')
                input(self.__better_view.display_message('Press any key to return'))
                return
        self.__better_view.display_message('Better not found!')
        input(self.__better_view.display_message('Press any key to return'))
    
    def update_better(self):
        better_id = self.__better_view.get_by_id()
        for better in self.__better_dao.get_all():
            if better.id == better_id:
                new_data_better = self.__better_view.get_better_info()
                better.name = new_data_better["name"]
                better.nick = new_data_better["nick"]
                better.cpf = new_data_better["cpf"]
                better.wallet = new_data_better["wallet"]
                self.__better_dao.update(better)
            else:
                self.__better_view.display_message('better not found!')

    def delete_better(self):
        better_id = self.__better_view.get_by_id()
        for better in self.__better_dao.get_all():
            if better.id == better_id:
                for bet in better.bets:
                    self.__system_controller.bet_controller.delete_bet_by_id(bet.id)
                self.__better_dao.remove(better.id)
                input(self.__better_view.display_message('Better deleted succesfully!'))
                return
        self.__better_view.display_message('Better not found!')
        input(self.__better_view.display_message('Press any key to return'))

    def backtrack(self):
        self.__system_controller.admin_controller.display_screen()

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

    def display_balance_and_bets(self):
        better_id = self.__better_view.get_by_id()
        better = self.get_better_by_id(better_id)
        if better == None:
            self.__better_view.display_message("Better not found!!")    
            input()
            return
        self.__better_view.display_message(f' {better.name}')
        self.__better_view.display_message("Balance:")
        self.__better_view.display_message(f" {better.wallet} ")   
        for bet in better.bets:
            self.__better_view.display_message(f'Bet ID: {bet.id}')
            self.__better_view.display_message(f'Bet Game: {bet.game.name}')
            self.__better_view.display_message(f'Bet Price: {bet.price}')
            self.__better_view.display_message(f'Bet Outcome: {bet.result.outcome}')
            if not bet.result.outcome == 'Draw':
                self.__better_view.display_message(f'Bet Player: {bet.result.player.name}')
        input()
        return
    
