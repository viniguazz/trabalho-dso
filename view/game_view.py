import PySimpleGUI as sg
from view.abstract_view import AbstractView


class GameView(AbstractView):

    def __init__(self):
        super().__init__()

    def display_options(self):
        self.init_components()
        button, values = self.__window.Read()
        opcao = 0
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        if values['4']:
            opcao = 4
        if values['5']:
            opcao = 5
        if values['6'] or button in (None,'Cancelar'):
            opcao = 6
        self.close()
        return opcao
    
    def get_game_info(self):
        layout = [
            [sg.Text('Inform the GAME data:')],
            [sg.Text('Name:'), sg.InputText('', key = 'name')],
            [sg.Text('Player 1\'s ID:'), sg.InputText('', key = 'player1_id')],
            [sg.Text('Player2\'s ID'), sg.InputText('', key = 'player2_id')],
            [sg.Button('Confirmar') , sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('getgameinfo').Layout(layout)

        button, values = self.open()
        name = values['name']
        player1_id = int(values['player1_id'])
        player2_id = int(values['player2_id'])

        self.close()
        return {'name': name, 'player1_id': player1_id, 'player2_id': player2_id}
        
    def list_games(self, games):
        string_all_games = ""
        for game in games:
            if not game.result == None:
                if not game.result.outcome == 'Draw':
                    string_all_games = string_all_games + "ID: " + str(game.id) +'\n'
                    string_all_games = string_all_games + "Name: " + game.name +'\n'
                    string_all_games = string_all_games + "Outomce: " + (game.result.outcome) +'\n'
                    string_all_games = string_all_games + "Player: " + (game.result.player) +'\n'
                else:
                    string_all_games = string_all_games + "ID: " + str(game.id) +'\n'
                    string_all_games = string_all_games + "Name: " + game.name +'\n'
                    string_all_games = string_all_games + "Outcome: " + str(game.result.outcome) +'\n'
            else:
                    string_all_games = string_all_games + "ID: " + str(game.id) +'\n'
                    string_all_games = string_all_games + "Name: " + game.name +'\n'
                    string_all_games = string_all_games + "Result: " + str(game.result) +'\n'
            if len(games) == 0:
                string_all_games = string_all_games + 'No Games Found'
        sg.Popup('============ LIST GAMES ============', string_all_games)

    def get_by_id(self):
        layout = [
            [sg.Text('Inform the ID:')],
            [sg.Text('ID:'), sg.InputText('', key ='id')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('getgameid').Layout(layout)

        button, values = self.open()
        id = values['id']
        self.close()
        return int(id)
    

    def init_components(self):
        layout = [
            [sg.Text('============ CRUD GAMES ============')],
            [sg.Radio('Create', "RD1", key = '1')],
            [sg.Radio('Read', "RD1", key='2')],
            [sg.Radio('Update', "RD1", key = '3')],
            [sg.Radio('Delete', "RD1", key = '4')],
            [sg.Radio('List', "RD1", key='5')],
            [sg.Radio('Return', "RD1", key = '6')],
            [sg.Button('Submit'), sg.Cancel('Cancel')]
        ]
        self.__window = sg.Window('gameview').Layout(layout)

    def get_result_info(self):
        layout = [
            [sg.Text('Inform the Result Data')],
            [sg.Radio('Victory', "RD1", key = '1')],
            [sg.Radio('Draw', "RD1", key='2')],
            [sg.Radio('Player1', "RD2",key = '3')],
            [sg.Radio('Player2', "RD2", key = 4)],
            [sg.Button('Confirmar', sg.Cancel('Cancelar'))]
        ]
        player = None
        button, values = self.open()
        if values['1']:
            outcome = 'Victory'
        if values['2']:
            outcome = 'Draw'
        if values['3']:
            player = 'player1'
        if values['4']:
            player = 'player2'
        if outcome == 'Draw':
            player = None

        self.close()
        return {'outcome' : outcome, 'player' : player}
    
    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values
        

    # def get_result_info(self):
    #     self.clear_screen()
    #     print()
    #     print('Inform the Result data:')
    #     outcome = self.get_outcome()
    #     if outcome == 'Draw':
    #         player = None
    #         return {'outcome' : outcome, 'player' : player}
    #     player = self.get_player()
    #     return {'outcome' : outcome, 'player' : player}

    # def get_outcome(self):
    #     self.clear_screen()
    #     print ("1) Draw")
    #     print ("2) Victory")
    #     outcome = int(input())

    #     while outcome not in (1,2):
    #         self.clear_screen()
    #         print("Follow the instructions!")
    #         print ("1) Draw")
    #         print ("2) Victory")
    #         outcome = int(input())
    #     if outcome == 1:
    #         return 'Draw'
    #     else:
    #         return 'Victory'
    
    # def get_player(self):
    #     self.clear_screen()
    #     print ("1) Player1")
    #     print ("2) Player2")
    #     player = int(input())

    #     while player not in (1,2):
    #         self.clear_screen()
    #         print("Follow the instructions!")
    #         print ("1) Player1")
    #         print ("2) Player2")
    #         player = int(input())
    #     if player == 1:
    #         return 'player1'
    #     else:
    #         return 'player2'