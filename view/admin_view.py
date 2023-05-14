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
        while True:
            try:
                option = int(input('>>> '))
                if option in (1,2,3,4,5):
                    return option
                else: 
                    print("Let's Try again, shall we?")
            except:
                raise Exception('C\'mon... Gimme some real numbers')