from time import sleep
from model import Bet, Result, Player
from view import BetView
from repository import BetDAO
from exception import InvalidNativeTypeException, InvalidGameException, InvalidBetterException, InvalidResultException, ClosedGameException, CancelOperationException, NoMenuSelected


class BetController():
    def __init__(self, system_controller):
        self.__system_controller = system_controller
        self.__bet_view = BetView()
        self.__bet_dao = BetDAO()

    def list_bets(self):
        self.__bet_view.list_bets(self.__bet_dao.get_all())
        self.display_screen()

    #revisar a questão do inspect
    def add_bet(self):
        try:
            bet_data = self.__bet_view.get_bet_info()
            if bet_data == None:
                raise CancelOperationException
            bet_game = self.__system_controller.game_controller.get_by_id(int(bet_data["game_id"]))
            bet_price = bet_data["price"]
            bet_better = self.__system_controller.better_controller.get_better_by_id(bet_data["better_id"])
            bet_result = Result(bet_data["result"]["outcome"], bet_data["result"]["player"])
            bet_odds = bet_data['odd']
            bet_id = self.__bet_dao.get_current_id()
            new_bet = bet_game.add_bet(bet_id, bet_price, bet_better, bet_result, bet_odds)
            bet_better.remove_money(bet_price)
            self.__bet_dao.add(new_bet)
            self.__system_controller.game_controller.save_game(bet_game)
            self.__system_controller.better_controller.save_better(bet_better) 
            self.__bet_view.display_message(f'Bet Created! ID: {bet_id}')
            return
        except (InvalidNativeTypeException, InvalidGameException, InvalidBetterException, InvalidResultException, ClosedGameException) as e:
            self.__bet_view.display_message(e)
            return
        except CancelOperationException:
            return


    #Usar como base
    def read_bet(self):
        bet_id = self.__bet_view.get_by_id()
        try:
            if bet_id == None:
                raise CancelOperationException
            for bet in self.__bet_dao.get_all():
                if bet.id == bet_id:
                    message = f'ID: {bet.id}\nGame: {bet.game.name}\nPrice: {bet.price}\nOutcome: {bet.result.outcome}\nPlayer: {bet.result.player}\nOdd: {bet.odd}'
                    self.__bet_view.display_message(message)
                    return
            self.__bet_view.display_message('bet not found!')
        except (CancelOperationException):
            return


    def save_bet(self, bet):
        self.__bet_dao.update(bet)

    def delete_bet(self):
        bet_id = self.__bet_view.get_by_id()
        try:
            if bet_id == None:
                raise CancelOperationException
            for bet in self.__bet_dao.get_all():
                if bet.id == bet_id:
                    if bet.status == True:
                        bet.better.add_money(bet.price)
                    bet.game.remove_bet(bet.id)
                    self.__system_controller.game_controller.save_game(bet.game)
                    self.__bet_dao.remove(bet.id)
                    self.__bet_view.display_message("Bet Deleted!")
                    return
            self.__bet_view.display_message('bet not found!')
            return
        except(CancelOperationException):
            return

    
    def delete_bet_by_id(self, id):
        bet_id = id
        try:
            if bet_id == None:
                raise CancelOperationException
            for bet in self.__bet_dao.get_all():
                if bet.id == id:
                    bet.game.remove_bet(bet.id)
                    self.__system_controller.game_controller.save_game(bet.game)
                    self.__bet_dao.remove(bet.id)
                    self.__bet_view.display_message("Bet Deleted!")
                    return
            self.__bet_view.display_message('bet not found!')
            return
        except(CancelOperationException):
            return


    def backtrack(self):
        self.__system_controller.admin_controller.display_screen()

    def list_display(self):
        self.list_bets()
        self.__system_controller.display_screen()

    #Verificar Retirada
    # def display_place_bet(self):
    #     option = self.__bet_view.display_add_bet()
    #     if option == 2:
    #         self.__system_controller.display_screen()
    #     elif option == 1:
    #         self.add_bet()

    def display_screen(self):
        try:
            option_list = {0 : self.backtrack,
            1: self.add_bet, 
            2: self.read_bet, 
            3: self.delete_bet, 
            4: self.list_bets, 
            5: self.backtrack}

            while True:
                option = self.__bet_view.display_options()
                selected_function = option_list[option]
                selected_function()
        except(NoMenuSelected) as e:
            self.__bet_view.display_message(e)
            self.display_screen()

    def all_bets(self):
        return self.__bet_dao.get_all()

