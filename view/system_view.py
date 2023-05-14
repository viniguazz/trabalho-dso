import os

class SystemView:
    
    def display_options(self):
        os.system('cls')
        print("====================== HELL BETS ======================")
        print()
        print("Choose your destiny:")
        print()
        print("1) View Current Games")
        print("2) Place Bet")
        print("3) Check Bets and Balance")
        print("4) Admin - CRUD Players, Users, Bets and Games")
        print("5) Exit")
        print()
        print('=======================================================')

        while True:
            try {
                option = int(input('>>> '))
                return option
                
            } except {
                raise Exception('C\'mon... Gimme some real numbers')
            }
        


        