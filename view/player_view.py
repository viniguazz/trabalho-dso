
class PlayerView():

    def display_options(self):
        os.system('cls')
        print("============ CRUD PLAYER ============")
        print('1) CREATE')
        print('2) READ')
        print('3) UPDATE')
        print('4) DELETE')
        print('5) LIST')
        print('6) Return')

    def display_message(message):
        print(message)
    
    def get_player_info(self):
        os.system('cls')
        print()
        print('Inform the PLAYER data:')
        name = input('Name:')
        victories = input('Number of victories:')
        losses = input('Number of losses:')
        draws = input('Number of draws:')
        return {'name': name, 'victories': victories, 'losses': losses, 'draws': draws}

    def get_by_id(self):
        print('Inform the ID:')
        id = input(id)
        return id