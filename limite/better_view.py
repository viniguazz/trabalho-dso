import os

class BetterView:

    def display_screen(self):
        os.system('cls')
        print()
        print('Bets:')
        print()
        print(f'| id: {game_data['id']}   | Status: {game_data['status']}  | Bets: {game_data['bets']}      | P1: {game_data['player']}             | P2: {game_data['player']}            |')
        print()
        print('Balance:')

