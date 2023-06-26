from model import Game, Result
from view import GameView
from repository import GameDAO
from exception import InvalidNativeTypeException, InvalidPlayerException, InvalidGameException, NoMenuSelected, CancelOperationException


class GameController():

    def __init__(self, system_controller):
        self.__system_controller = system_controller
        self.__game_view = GameView()
        self.__game_dao = GameDAO()

    @property
    def games(self):
        return self.__game_dao.get_all()

    def get_by_id(self, id):
        for game in self.__game_dao.get_all():
            if game.id == id:
                return game
        raise InvalidGameException(id)
        return

    def list_games(self):
        self.__game_view.list_games(self.__game_dao.get_all())
        return
    
    def add_game(self):
        try:
            game_data = self.__game_view.get_game_info()
            if game_data == None:
                raise CancelOperationException
            game_name = game_data['name']
            player1 = self.__system_controller.player_controller.get_player_by_id(game_data['player1_id'])
            player2 = self.__system_controller.player_controller.get_player_by_id(game_data['player2_id'])
            current_base_id = self.__game_dao.get_current_id()
            try:
                new_game = Game(current_base_id, game_name, player1, player2)
            except (InvalidNativeTypeException, InvalidPlayerException) as e:
                self.__game_view.display_message(e)
                return
            if new_game not in self.__game_dao.get_all():
                self.__game_dao.add(new_game)           
                self.__game_view.display_message(f'New game create succesfully! ID:{new_game.id}')
                return
            else:
                self.__game_view.display_message("Game already in database")
                return
        except CancelOperationException:
            return
    
    def read_game(self):
        game_id = self.__game_view.get_by_id()
        try:
            if game_id == None:
                raise CancelOperationException
            for game in self.__game_dao.get_all():
                if game.id == game_id:
                    message = f'ID: {game.id}\nName: {game.name}\nPlayer1: {game.player1.name}\Player2: {game.player2.name}'
                    self.__game_view.display_message(message)
                    return
            self.__game_view.display_message('game not found!')
        except CancelOperationException:
            return 
    
    def update_game(self):
        game_id = self.__game_view.get_by_id()
        try:
            if game_id == None:
                raise CancelOperationException
            player = None
            for game in self.__game_dao.get_all():
                if game.id == game_id:
                    if game.result == None:
                        result_data = self.__game_view.get_result_info()
                        if result_data == None:
                            raise CancelOperationException
                        if result_data["player"] == 'player1':
                            player = game.player1
                        elif result_data["player"] == 'player2':
                            player = game.player2
                        game.result = Result(result_data["outcome"], player)
                        self.__game_dao.update(game)
                        for bet in game.bets: 
                            self.__system_controller.better_controller.save_better(bet.better)
                            self.__system_controller.bet_controller.save_bet(bet)
                        self.__game_view.display_message(f'Game {game_id} Ended!')
                        return
                    else:
                        self.__game_view.display_message('Game already ended!')
                        return
            self.__game_view.display_message('Game not found!')
            return
        except CancelOperationException:
            return

    def save_game(self, game):
        self.__game_dao.update(game)
    
    def delete_game(self):
        game_id = self.__game_view.get_by_id()
        try:
            if game_id == None:
                raise CancelOperationException
            for game in self.__game_dao.get_all():
                if game.id == game_id:
                    for bet in game.bets.copy():
                        if game.result == None:
                            bet.better.add_money(bet.price)
                            self.__system_controller.better_controller.save_better(bet.better)
                        self.__system_controller.bet_controller.delete_bet_by_id(bet.id)
                    self.__game_dao.remove(game.id)
                    self.__game_view.display_message('Game deleted succesfully!')
                    return
            self.__game_view.display_message('Game not found!')
            return
        except CancelOperationException:
            return

    def backtrack(self):
        self.__system_controller.admin_controller.display_screen()

    def list_display(self):
        self.list_games()
        self.__system_controller.display_screen()

    def display_screen(self):
        try:
            option_list = {0: self.backtrack,
            1: self.add_game, 
            2: self.read_game, 
            3: self.update_game, 
            4: self.delete_game, 
            5: self.list_games, 
            6: self.backtrack}

            while True:
                option = self.__game_view.display_options()
                selected_function = option_list[option]
                selected_function()
        except(NoMenuSelected) as e:
            self.__game_view.display_message(e)
            self.display_screen()


    