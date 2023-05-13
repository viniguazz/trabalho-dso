import os

class Admin():

    def login(self):
        password = input('PASSWORD:')
        return password
    
    def show_options(self):
        os.system('cls')
        print("============ ADMIN OPTIONS ============")
        print('1) CRUD Players')
        print('2) CRUD Users')
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
        print("============ CRUD USERS ============")
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
    
    def get_player_infor(self):
        