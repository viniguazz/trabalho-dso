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
                raise Exception('C\'mon... Gimme some real numbers')
            


    def display_message(message):
        print(message)
    
    def get_game_info(self):
        os.system('cls')
        print()
        print('Inform the game data:')
        name = input('Name:')
        player1_id = input('Player 1\'s ID:')
        player2_id = input('Player 2\'s ID:')
        return {'name': name, 'player1_id': player1_id, 'player2_id': player2_id}

    def get_by_id(self):
        print('Inform the ID:')
        id = input(id)
        return id
    
    def clear_screen():
        os.system('cls')