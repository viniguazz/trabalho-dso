import os

class GameListView:
    
    def display_game(self, game_data):
        print(f'| id: {game_data.id()}   | Status: {game_data.status()}  | Bets: {game_data.bets()}      | P1: {game_data.player1()}             | P2: {game_data.player2()}            |')