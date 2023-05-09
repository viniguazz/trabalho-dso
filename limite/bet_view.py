import os

class BetView():

    def place_bet():
        os.system('cls')
        print()
        print('Inform the bet data:')
        game_id = input('Game id:')
        price = input('Price:')
        result = input('Result: 0: Victory 1: Loss 2: Draw')
        return {"game_id": game_id, "price": price, "result": result}

