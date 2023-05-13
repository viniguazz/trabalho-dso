import os

class SystemView:
    
    def display_options(self):
        
        os.system('cls')

        print("============ HELL BETS ============")
        print()
        print("Choose your destiny:")
        print()
        print("1) View Games")
        print("2) Place Bet")
        print("3) Check Bets and Balance")
        print("4) Register/Update/Exclude Players, Users, Bets and Games")

        while True:
            try {
                opcao = int(input())
                return opcao
                
            } except {
                raise Exception('f*** off. gimme some real f******* numbers')
            }
        


        