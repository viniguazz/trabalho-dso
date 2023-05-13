from player import Player
from stats import Stats
from player_view import PlayerView

class PlayerController():

    def __init__(self, system_controller):
        self.__admin_controller = admin_controller
        self.__player_view = PlayerView()
        self.__players = []

    def get_player_by_id(self, id):
        for player in self.__players:
            if id == player.id:
                return player
        print('Invalid player!')
        return None
    
    def list_players(self):
        for player in self.__player:
            print('===========================================')
            self.__player_view.display_message(f'ID: {player.id}, 
            Name: {player.name}, 
            Victories: {player.stats.victories},
            Losses: {player.stats.losses},
            Draws: {player.stats.draws}')
            print('===========================================')
        input('Press any key to return...')
    
    def add_player(self):
        player_data = get_player_info()
        player_name = player_data['name']
        victories = player_data['victories']
        losses = player_data['losses']
        draws = player_data['draws']
        stats = Stats(victories, losses, draws)
        new_player = Player(player_name, stats)
        unique = True
        for player in self.__players:
            if player.name == player_name:
                unique = False
        if unique:
            self.__players.append(new_player)
            print(f'New player create succesfully! ID:{new_player.id}')
        else:
            print('Player already in the database! Process failed!')
    
    def read_player(self):
        player_id = self.__player_view.get_by_id()
        for player in self.__players:
            if game['id'] == game_id:
                os.system('cls')
                print(f'ID: {player['id']}')
                print(f'Name: {player['name']}')
                print(f'victories: {player['victories']}')
                print(f'losses: {player['losses']}')
                print(f'draws: {player['draws']}')
                input('Press any key to return')
                return
        print('Player not found!')
        input('Press any key to return')
    
    #incompleto assim como o de game
    def update_player(self):
        player_id = self.__game_view.get_bet_by_id()
        for game in self.__games:
            if game['id'] == game_id:

    def delete_player(self):
        player_id = self.__player_view.get_bet_by_id()
        for player in self.__players:
            if player['id'] == player_id:
                players.remove(player)
                input('Player deleted succesfully!')
                return
        print('Player not found!')
        input('Press any key to return')

    def backtrack(self):
        self.__admin_controller.display_screen()

    def display_screen(self):
        option_list = {1: self.add_player, 
        2: self.read_player, 
        3: self.update_player, 
        4: self.delete_player, 
        5: self.list_player, 
        6: self.backtrack}

        while True:
            option = self.__player_view.display_options()
            selected_function = option_list[option]
            selected_function()
