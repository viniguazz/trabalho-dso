import PySimpleGUI as sg
from view.abstract_view import AbstractView
from exception import NoMenuSelected, CancelOperationException, EmptyInputException

class GameView(AbstractView):

    def __init__(self):
        self.__window = None
        self.init_components()

    def display_options(self):
        self.init_components()
        button, values = self.__window.Read()
        opcao = 0
        if values['1'] and button in ('Confirmar', None):
            opcao = 1
        elif values['2'] and button in ('Confirmar', None):
            opcao = 2
        elif values['3'] and button in ('Confirmar', None):
            opcao = 3
        elif values['4'] and button in ('Confirmar', None):
            opcao = 4
        elif values['5'] and button in ('Confirmar', None):
            opcao = 5
        elif values['6'] or button in (None, 'Cancelar'):
            opcao = 6
        elif button in ('Confirmar', None):
            raise NoMenuSelected
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
        try:
            button, values = self.open()

            if button in (None, 'Cancelar'):
                raise CancelOperationException
            if any in values is None:
                raise EmptyInputException
            name = values['name']
            player1_id = int(values['player1_id'])
            player2_id = int(values['player2_id'])
            self.close()
            return {'name': name, 'player1_id': player1_id, 'player2_id': player2_id}
        except (CancelOperationException) as e:
            self.display_message(e)
            self.close()
            return None
        except (EmptyInputException) as e:
            self.display_message(e)
            self.close()
            return self.get_game_info()
        except:
            self.close()
            self.display_message("Please insert valid types")
            return self.get_game_info()

        
        
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

        try:
            button, values = self.open()
                        
            if button in (None, 'Cancelar'):
                raise CancelOperationException
            if any in values is None:
                raise EmptyInputException
            id = values['id']
            self.close()
            return int(id)
        except (CancelOperationException) as e:
            self.display_message(e)
            self.close()
            return None
        except (EmptyInputException) as e:
            self.display_message(e)
            self.close()
            return self.get_by_id()
        except:
            self.close()
            self.display_message("Please insert valid types")
            return self.get_by_id()
        
    def init_components(self):
        layout = [
            [sg.Text('============ CRUD GAMES ============')],
            [sg.Radio('Create', "RD1", key = '1')],
            [sg.Radio('Read', "RD1", key='2')],
            [sg.Radio('Update', "RD1", key = '3')],
            [sg.Radio('Delete', "RD1", key = '4')],
            [sg.Radio('List', "RD1", key='5')],
            [sg.Radio('Return', "RD1", key = '6')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('gameview').Layout(layout)

    def get_result_info(self):
        layout = [
            [sg.Text('Inform the Result Data')],
            [sg.Radio('Victory', "RD1", key = '1')],
            [sg.Radio('Draw', "RD1", key='2')],
            [sg.Radio('Player1', "RD2",key = '3')],
            [sg.Radio('Player2', "RD2", key = 4)],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('getresultinfo').Layout(layout)

        try:
            player = None
            button, values = self.open()
            if button in (None, 'Cancelar'):
                    raise CancelOperationException
            if values['2']:
                outcome = 'Draw'
                player = None
                self.close()
                return {'outcome' : outcome, 'player' : player}
            if values['3'] and values['1']:
                player = 'player1'
                self.close()
                return {'outcome' : outcome, 'player' : player}
            if values['4'] and values['1']:
                player = 'player2'
                self.close()
                return {'outcome' : outcome, 'player' : player}
            if button in ('Confirmar', None):
                raise NoMenuSelected

            self.close()
            return {'outcome' : outcome, 'player' : player}
        
        except (CancelOperationException) as e:
            self.display_message(e)
            self.close()
            return None
        except (NoMenuSelected) as e:
            self.display_message(e)
            self.close()
            return self.get_result_info()
        except:
            self.close()
            self.display_message("Please insert valid types")
            return self.get_result_info()
    
    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values