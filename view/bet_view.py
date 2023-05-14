import os

class BetView():

    def display_message(message):
        print(message)

    def clear_screen(self):
        os.system('cls')

    def display_options(self):
        os.system('cls')
        print("============ TIME TO LOSE MONEY! ============")
        print()
        print("1) Place bet")
        print("2) Return")
        while True:
            try :
                opcao = int(input())
                return opcao
                
            except:
                raise Exception('f*** off. gimme some real f******* numbers')


    def place_bet():
        os.system('cls')
        print()
        print('Inform the bet data:')
        better_id = input('Better Id:')
        game_id = input('Game id:')
        price = input('Price:')
        result = input('')
        
        return {"game_id": game_id, "price": price, "result": result, "better_id": better_id}

    def display_options(self):
        print("============ STATS ============")
        print("1) Check bets and Funds")
        print("2) Return")
        while True:
            try:
                option = int(input())
                return option
            except:
                raise Exception('f*** off. gimme some real f******* numbers')
    
    def get_better_info(self):
        os.system('cls')
        print()
        print('Inform the better data:')
        name = input('Name:')
        nick = input('Nick:')
        wallet = input('Funds:')
        cpf = input('CPF:')
        return {'name': name, 'nick': nick, 'wallet': wallet, 'cpf': cpf}
    
    
    def get_better(self):
        os.system('cls')
        print()
        better_id = input('Inform the better\'s ID:')
        return better_id

    def display_better_data(self, better):
        os.system('cls')
        print()
        print('Bets')
        print()
        for bet in better["bets"]:
            print(f'| Price: {bet["price"]}   | Game: {bet["game"]}  | result: {bet["result"]}       ')
        print()
        print('Balance:')
        print()
        print(better['wallet'])
        print()
        input('Press any key to ')

    
    def get_by_id(self):
        print('Inform the ID:')
        id = input(id)
        return id
    
    def get_game_info(self):
        os.system('cls')
        print()
        print('Inform the game data:')
        name = input('Name:')
        player1_id = input('Player 1\'s ID:')
        player2_id = input('Player 2\'s ID:')
        return {'name': name, 'player1_id': player1_id, 'player2_id': player2_id}