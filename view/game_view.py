import os

class GameView():

    def display_options(self):
        os.system('cls')
        print("============ CRUD GAMES ============")
        print('1) CREATE')
        print('2) READ')
        print('3) UPDATE')
        print('4) DELETE')
        print('5) LIST')
        print('6) Return')
        while True:
            try:
                option = int(input('>>> '))
                if option in (1,2,3,4,5,6):
                    return option
                else: 
                    print("Let's Try again, shall we?")
            except:
                print("Please insert a number!")
            


    def display_message(self, message):
        print(message)
    
    def get_game_info(self):
        os.system('cls')
        print()
        print('Inform the game data:')
        name = input('Name:')
        player1_id = int(input('Player 1\'s ID:'))
        player2_id = int(input('Player 2\'s ID:'))
        return {'name': name, 'player1_id': player1_id, 'player2_id': player2_id}

    def get_by_id(self):
        print('Inform the ID:')
        id = int(input(">>>"))
        return id
    
    def clear_screen(self):
        os.system('cls')

    def get_result_info(self):
        self.clear_screen()
        print()
        print('Inform the Result data:')
        outcome = self.get_outcome()
        if outcome == 'Draw':
            player = None
            return {'outcome' : outcome, 'player' : player}
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
            return 'player1'
        else:
            return 'player2'