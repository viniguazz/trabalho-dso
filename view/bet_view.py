import os

class BetView():

    def display_message(message):
        print(message)

    def clear_screen(self):
        os.system('cls')

    def display_options(self):
        self.clear_screen()
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

    def place_bet(self):
        self.clear_screen()
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
    
    def get_bet_info(self):
        os.system('cls')
        print()
        print('Inform the bet data:')
        game_id = input('Game ID:')
        price = input('Price: ')
        result = self.get_result_info()
        cpf = input('CPF: ')
        #better
        return {'game_id': game_id, 'price': price, 'result': result, 'cpf': cpf}
    
    
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
    
    def get_result_info(self):
        self.clear_screen()
        print()
        print('Inform the Result data:')
        outcome = self.get_outcome()
        player = self.get_player()
        return {'outcome' : outcome, 'player' : player}


    def get_outcome(self):
        self.clear_screen()
        print ("1) Draw")
        print ("2) Victory")
        outcome = int(input())

        while outcome not in (1,2):
            self.clear_screen()
            print("Follow the instructions!")
            print ("1) Draw")
            print ("2) Victory")
            outcome = int(input())

        if outcome == 1:
            return 'Draw'
        else:
            return 'Victory'
    
    def get_player(self):
        self.clear_screen()
        print ("1) Player1")
        print ("2) Player2")
        player = int(input())

        while player not in (1,2):
            self.clear_screen()
            print("Follow the instructions!")
            print ("1) Player1")
            print ("2) Player2")
            player = int(input())

        if player == 1:
            return 'Player1'
        else:
            return 'Player2'