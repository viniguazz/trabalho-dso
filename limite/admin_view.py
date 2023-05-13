import os

class AdminView():

    def login(self):
        os.system('cls')
        password = input('Please insert the master PASSWORD:')
        return password
    
    def show_options(self):
        os.system('cls')
        print("============ ADMIN OPTIONS ============")
        print('1) CRUD Players')
        print('2) CRUD Betters')
        print('3) CRUD Games')
        print('4) CRUD Bets')
        print('5) Return')

        option = input('>>> ')
        return option