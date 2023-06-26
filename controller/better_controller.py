from model import Better
from view import BetterView
from repository import BetterDAO
from exception import InvalidBetterException, NoMenuSelected,CancelOperationException


class BetterController():
    def __init__(self, system_controller):
        self.__system_controller = system_controller
        self.__better_view = BetterView()
        self.__better_dao = BetterDAO()
    
    @property
    def betters(self):
        return self.__better_dao.get_all()
   

    def get_better_by_id(self, id):
        for better in self.__better_dao.get_all():
            if id == better.id:
                return better
        raise InvalidBetterException(id)
        return 
    
    def list_betters(self):
        self.__better_view.list_better(self.__better_dao.get_all())     
        self.display_screen()

    def add_better(self):
        try:
            better_data = self.__better_view.get_better_info()
            if better_data == None:
                raise CancelOperationException
            better_name = better_data['name']
            better_nick = better_data['nick']
            better_cpf = better_data['cpf']
            better_funds = better_data['wallet']
            current_base_id = self.__better_dao.get_current_id()
            new_better = Better(current_base_id, better_name, better_nick, better_funds, better_cpf)
            if new_better not in self.__better_dao.get_all():
                self.__better_dao.add(new_better)
                self.__better_view.display_message(f'New better create succesfully! ID:{new_better.id}')
            else:
                self.__better_view.display_message('Better already in the database! Process failed!')
        except(CancelOperationException):
            return

    def read_better(self):
        better_id = self.__better_view.get_by_id()
        try:
            if better_id == None:
                raise CancelOperationException
            for better in self.__better_dao.get_all():
                if better.id == better_id:
                    message = f'ID: {better.id}\nName: {better.name}\nNick: {better.nick}\nCPF: {better.cpf}\nFunds: {better.wallet}\n'
                    self.__better_view.display_message(message)
                    return
            self.__better_view.display_message('better not found!')
        except(CancelOperationException):
            return
        
    def update_better(self):
        better_id = self.__better_view.get_by_id()
        try:
            if better_id == None:
                raise CancelOperationException
            for better in self.__better_dao.get_all():
                if better.id == better_id:
                    new_data_better = self.__better_view.get_better_info()
                    if new_data_better == None:
                        raise CancelOperationException
                    better.name = new_data_better["name"]
                    better.nick = new_data_better["nick"]
                    better.cpf = new_data_better["cpf"]
                    better.wallet = new_data_better["wallet"]
                    self.__better_dao.update(better)
                    return
            self.__better_view.display_message('better not found!')
        except(CancelOperationException):
            return
    


    def save_better(self, better):
        self.__better_dao.update(better)

    def delete_better(self):
        better_id = self.__better_view.get_by_id()
        try:
            if better_id == None:
                raise CancelOperationException
            for better in self.__better_dao.get_all():
                if better.id == better_id:
                    for bet in better.bets:
                        self.__system_controller.bet_controller.delete_bet_by_id(bet.id)
                    self.__better_dao.remove(better.id)
                    self.__better_view.display_message('Better deleted succesfully!')
                    return
            self.__better_view.display_message('Better not found!')
        except:
            return
            


    def backtrack(self):
        self.__system_controller.admin_controller.display_screen()

    def display_screen(self):
        try:
            option_list = {0:self.backtrack,
            1: self.add_better, 
            2: self.read_better, 
            3: self.update_better, 
            4: self.delete_better, 
            5: self.list_betters, 
            6: self.backtrack}

            while True:
                option = self.__better_view.display_options()
                selected_function = option_list[option]
                selected_function()
        except(NoMenuSelected) as e:
            self.__better_view.display_message(e)
            self.display_screen()


    def display_balance_and_bets(self):
        better_id = self.__better_view.get_by_id()
        try:
            if better_id == None:
                raise CancelOperationException
            better = self.get_better_by_id(better_id)
        except InvalidBetterException as e:
            self.__better_view.display_message(e)    
            return
        except CancelOperationException:
            return
        self.__better_view.display_better_data(better, self.__system_controller.bet_controller.all_bets())
        return