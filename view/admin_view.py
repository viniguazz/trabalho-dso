import os

class AdminView():

    def login(self):
        os.system('cls')
        password = input('Please insert the master PASSWORD:')
        return password
    
    def display_options(self):
        self.clear_screen()
        print("============ ADMIN OPTIONS ============")
        print('1) Crud Games')
        print('2) CRUD Players')
        print('3) CRUD Betters')
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
        
    def clear_screen(self):
        os.system('cls')