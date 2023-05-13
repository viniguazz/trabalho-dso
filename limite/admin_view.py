import os

class Admin():

    def login(self):
        password = input('PASSWORD:')
        return password
    
    def show_options(self):
        os.system('cls')
        print("============ ADMIN OPTIONS ============")
        print('1) CRUD Players')
        print('2) CRUD Betters')
        print('3) CRUD Games')
        print('4) CRUD Bets')
        print('5) Return')

        option = input()
        return option


    def crud_players(self):
        os.system('cls')
        print("============ CRUD PLAYERS ============")
        print('1) CREATE')
        print('2) READ')
        print('3) UPDATE')
        print('4) DELETE')
        print('5) LIST')
        print('6) Return')

        option = input()
        return option

    def crud_users(self):
        os.system('cls')
        print("============ CRUD BETTER ============")
        print('1) CREATE')
        print('2) READ')
        print('3) UPDATE')
        print('4) DELETE')
        print('5) LIST')
        print('6) Return')

        option = input()
        return option

    def crud_games(self):
        os.system('cls')
        print("============ CRUD GAMES ============")
        print('1) CREATE')
        print('2) READ')
        print('3) UPDATE')
        print('4) DELETE')
        print('5) LIST')
        print('6) Return')

        option = input()
        return option

    def crud_bets(self):
        os.system('cls')
        print("============ CRUD GAMES ============")
        print('1) CREATE')
        print('2) READ')
        print('3) UPDATE')
        print('4) DELETE')
        print('5) LIST')
        print('6) Return')

        option = input()
        return option

    def get_by_id(self):
        print('Inform the ID:')
        id = input(id)
        return id
    
    def get_player_info(self):
        os.system('cls')
        print()
        print('Inform the player data:')
        name = input('Name:')
        victories = input('Number of victories:')
        losses = input('Number of losses:')
        draws = input('Number of draws:')
        return {'name': name, 'victories': victories, 'losses': losses, 'draws': draws}

    def get_better_info(self):
        os.system('cls')
        print()
        print('Inform the better data:')
        nick = input('Nick:')
        wallet = input('Funds:')
        cpf = input('CPF:')
        return {'nick': nick, 'wallet': wallet, 'cpf': cpf}

    def get_game_info(self):
        os.system('cls')
        print()
        print('Inform the game data:')
        name = input('Name:')
        player1_id = input('Player 1\'s ID:')
        player2_id = input('Player 2\'s ID:')
        return {'name': name, 'player1_id': player1_id, 'player2_id': player2_id}

    def get_bet_info(self):
        os.system('cls')
        print()
        print('Inform the bet data:')
        price = input('Price:')
        game = input('Game ID:')
        better = input('Better ID:')
        result = input('Draw (0) or Victory (1)?')
        if result == 1:
            player = input('Player1 (0) or Player2 (1)?')
            return {'price': price, 'game': game, 'better': better, 'result': result, 'player': player }
        return {'price': price, 'game': game, 'better': better, 'result': result}


    def deletion(self):
        os.system('cls')
        print("============ DELETE ============")
        print('1) CREATE')

    def confirm_deletion(self, object):

    def read(self):
        os.system('cls')
        print("============ CRUD GAMES ============")
        print('1) CREATE')

    