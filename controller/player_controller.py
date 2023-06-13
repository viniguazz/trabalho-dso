from model.player import Player
from model.stats import Stats
from view.player_view import PlayerView
from repository.player_dao import PlayerDAO

class PlayerController():

    def __init__(self, system_controller):
        self.__system_controller = system_controller
        self.__player_view = PlayerView()
        self.__player_dao = PlayerDAO()
        self.__id = 0

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self,id):
        self.__id = id

    def get_player_by_id(self, id):
        for player in self.__player_dao.get_all():
            if id == player.id:
                return player
        self.__player_view.display_message('Invalid player!')
        return None
    
    def list_players(self):
        for player in self.__player_dao.get_all():
            self.__player_view.display_message(f'ID: {player.id}, Name: {player.name}, Victories: {player.stats.victories}, Losses: {player.stats.losses}, Draws: {player.stats.draws}')
        if len(self.__player_dao.get_all()) == 0:
            self.__player_view.display_message('No players found')
        self.__player_view.display_message('Press any key to return...')
        input()
    
    def add_player(self):
        player_data = self.__player_view.get_player_info()
        player_name = player_data['name']
        victories = player_data['victories']
        losses = player_data['losses']
        draws = player_data['draws']
        stats = Stats(victories, losses, draws)
        new_player = Player(self.__id,player_name, stats)
        self.id_plus()
        if new_player not in self.__player_dao.get_all():
            self.__player_dao.add(new_player)
            self.__player_view.display_message(f'New player create succesfully! ID:{new_player.id}')
            input()
        else:
            self.__player_view.display_message('Player already in the database! Process failed!')
            input()

    def id_plus(self):
        self.__id +=1    

    def read_player(self):
        player_id = self.__player_view.get_by_id()
        for player in self.__player_dao.get_all():
            if player.id == player_id:
                self.__player_view.clear_screen()
                self.__player_view.display_message(f'ID: {player.id}')
                self.__player_view.display_message(f'Name: {player.name}')
                self.__player_view.display_message(f'victories: {player.stats.victories}')
                self.__player_view.display_message(f'losses: {player.stats.losses}')
                self.__player_view.display_message(f'draws: {player.stats.draws}')
                input(self.__player_view.display_message('Press any key to return'))
                return
        self.__player_view.display_message('Player not found!')
        input(self.__player_view.display_message('Press any key to return'))
    
    def update_player(self):
        player_id = self.__player_view.get_by_id()
        for player in self.__player_dao.get_all():
            if player.id == player_id:
                new_data_player = self.__player_view.get_player_info()
                player.name = new_data_player["name"]
                player.stats.victories = new_data_player["victories"]
                player.stats.losses = new_data_player["losses"]
                player.stats.draws = new_data_player["draws"]
                self.__player_dao.update(player)
            else:
                self.__player_view.display_message('player not found!')

    def delete_player(self):
        player_id = self.__player_view.get_by_id()
        for player in self.__player_dao.get_all():
            if player.id == player_id:
                self.__player_dao.remove(player.id)
                input(self.__player_view.display_message('Player deleted succesfully!'))
                return
        self.__player_view.display_message('Player not found!')
        input(self.__player_view.display_message('Press any key to return'))

    def backtrack(self):
        self.__system_controller.admin_controller.display_screen()

    def display_screen(self):
        option_list = {1: self.add_player, 
        2: self.read_player, 
        3: self.update_player, 
        4: self.delete_player, 
        5: self.list_players, 
        6: self.backtrack}

        while True:
            option = self.__player_view.display_options()
            selected_function = option_list[option]
            selected_function()

