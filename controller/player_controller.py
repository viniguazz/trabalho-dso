from model.player import Player
from model.stats import Stats
from view.player_view import PlayerView

class PlayerController():

    def __init__(self, system_controller):
        self.__player_view = PlayerView()
        self.__players = []

    def get_player_by_id(self, id):
        for player in self.__players:
            if id == player.id:
                return player
        self.__player_view.display_message('Invalid player!')
        return None
    
    def list_players(self):
        for player in self.__players:
            self.__player_view.display_message(f'ID: {player.id}, Name: {player.name}, Victories: {player.stats.victories}, Losses: {player.stats.losses}, Draws: {player.stats.draws}')
        self.__player_view.display_message('Press any key to return...')
    
    def add_player(self):
        player_data = self.__player_view.get_player_info()
        player_name = player_data['name']
        victories = player_data['victories']
        losses = player_data['losses']
        draws = player_data['draws']
        stats = Stats(victories, losses, draws)
        new_player = Player(player_name, stats)
        if new_player not in self.__players:
            self.__players.append(new_player)
            self.__player_view.display_message(f'New player create succesfully! ID:{new_player.id}')
        else:
            self.__player_view.display_message('Player already in the database! Process failed!')
    
    def read_player(self):
        player_id = self.__player_view.get_by_id()
        for player in self.__players:
            if player['id'] == player_id:
                self.__player_view.clear_screen()
                self.__player_view.display_message(f'ID: {player["id"]}')
                self.__player_view.display_message(f'Name: {player["name"]}')
                self.__player_view.display_message(f'victories: {player["victories"]}')
                self.__player_view.display_message(f'losses: {player["losses"]}')
                self.__player_view.display_message(f'draws: {player["draws"]}')
                input(self.__player_view.display_message('Press any key to return'))
                return
        self.__player_view.display_message('Player not found!')
        input(self.__player_view.display_message('Press any key to return'))
    
    #incompleto assim como o de game
    def update_player(self):
        player_id = self.__player_view.get_by_id()
        for player in self.__players:
            if player['id'] == player_id:
                new_data_player = self.__player_view.get_player_info()
                player.__id = new_data_player["id"]
                player.__name = new_data_player["name"]
                player.__victories = new_data_player["victories"]
                player.__losses = new_data_player["losses"]
                player.__draws = new_data_player["draws"]
            else:
                self.__player_view.display_message('player not found!')

    def delete_player(self):
        player_id = self.__player_view.get_by_id()
        for player in self.__players:
            if player['id'] == player_id:
                self.__players.remove(player)
                input(self.__player_view.display_message('Player deleted succesfully!'))
                return
        self.__player_view.display_message('Player not found!')
        input(self.__player_view.display_message('Press any key to return'))

    def backtrack(self):
        self.__admin_controller.display_screen()

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
