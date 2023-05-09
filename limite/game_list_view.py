import os

class GameListView:
    
    def display_game(self, game_data):
        print(f'| id: {game_data['id']}   | Status: {game_data['status']}  | Bets: {game_data['bets']}      | P1: {game_data['player']}             | P2: {game_data['player']}            |')
    def display_options(self):
        os.system('cls')
        print("============ HELL BETS ============")
        print()
        print("Choose your destiny:")
        print()
        print("1) View Games")
        print("2) Place Bet")
        print("3) Check Bets and Balance")
        print("4) Register Users, Players and Games")

        while True:
            try {
                opcao = int(input("Escolha a opcao:"))
                return opcao
                
            } except {
                raise Exception('f*** off. gimme some real f******* numbers')
            }