import os

class BetView():

    def display_options(self):
        os.system('cls')
        print("============ TIME TO LOSE MONEY! ============")
        print()
        print("1) Place bet")
        print("2) Return")
        while True:
            try {
                opcao = int(input())
                return opcao
                
            } except {
                raise Exception('f*** off. gimme some real f******* numbers')
            }


    def place_bet():
        os.system('cls')
        print()
        print('Inform the bet data:')
        better_id = input('Better Id:')
        game_id = input('Game id:')
        price = input('Price:')
        result = input('')
        
        return {"game_id": game_id, "price": price, "result": result, "better_id": better}

