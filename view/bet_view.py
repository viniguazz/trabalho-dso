import PySimpleGUI as sg
from view import AbstractView
from exception import CancelOperationException, NoMenuSelected, EmptyInputException

class BetView(AbstractView):
    def __init__(self):
        self.__window = None
        self.init_components()

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values

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
        elif values['5'] or button in (None, 'Cancelar'):
            opcao = 5
        elif button in ('Confirmar', None):
             raise NoMenuSelected
        self.close()
        return opcao
    
    def get_bet_info(self):
        layout = [
            [sg.Text('Inform the BET data:')],
            [sg.Text('Game ID:'), sg.InputText('', key = 'game_id')],
            [sg.Text('Price:'), sg.InputText('', key = 'price')],
            [sg.Text('Outcome:')],
            [sg.Radio('Victory', "RD2", key = '1')],
            [sg.Radio('Draw', "RD2", key = '2')],
            [sg.Radio('Player1',"RD1", key = '3')],
            [sg.Radio('Player2', "RD1", key = '4')],
            [sg.Text('Better ID:'), sg.InputText('', key='betterid')],
            [sg.Text('Odds:'), sg.InputText('', key='odd')],
            [sg.Button('Confirmar') , sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('getbetinfo').Layout(layout)

        try:
            button, values = self.open()
            
            if button in (None, 'Cancelar'):
                raise CancelOperationException
            if any in values is None:
                raise EmptyInputException
            game_id = int(values['game_id'])
            price = float(values['price'])
            if values['2']:
                result = {'outcome' : 'Draw', 'player' : None}
            else:
                if values['3']:
                    player = 'Player1'
                if values['4']:
                    player = 'Player2'
                result = {'outcome' : 'Victory', 'player' : player}
            better_id = int(values['betterid'])
            odd = int(values['odd'])
            self.close()
            return {'game_id': game_id, 'price': price, 'result': result, 'better_id': better_id, 'odd' : odd}
        except (CancelOperationException) as e:
            self.display_message(e)
            self.close()
            return None
        except (EmptyInputException) as e:
            self.display_message(e)
            self.close()
            return self.get_bet_info()
        except:
            self.close()
            self.display_message("Please insert valid types")
            return self.get_bet_info()
        


    def get_by_id(self):
        layout = [
            [sg.Text('Inform the ID:')],
            [sg.Text('ID:'), sg.InputText('', key ='id')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('getbyid').Layout(layout)
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

    def list_bets(self, bets):
        string_bets = ""
        for bet in bets:
            if bet.result.outcome == 'Draw':
                string_bets = string_bets + "Bet Id: " + str(bet.id) +'\n'
                string_bets = string_bets + "Better Name: " + str(bet.better.name) +'\n'
                string_bets = string_bets + "Price: " + str(bet.price) +'\n'
                string_bets = string_bets + "Game: " + str(bet.game.name) +'\n'
                string_bets = string_bets + "Result: " + str(bet.result.outcome) +'\n'
                string_bets = string_bets + "Odd: " + str(bet.odd) +'\n'
            else:
                string_bets = string_bets + "Bet Id: " + str(bet.id) +'\n'
                string_bets = string_bets + "Better Name: " + str(bet.better.name) +'\n'
                string_bets = string_bets + "Price: " + str(bet.price) +'\n'
                string_bets = string_bets + "Game: " + str(bet.game.name) +'\n'
                string_bets = string_bets + "Result: " + str(bet.result.outcome) +'\n'
                string_bets = string_bets + "Player " + str(bet.result.player) + '\n'
                string_bets = string_bets + "Odd: " + str(bet.odd) +'\n'
        sg.popup('============ LIST BET ============', string_bets)

    def init_components(self):
        layout = [
            [sg.Text('"============ CRUD BET ============')],
            [sg.Radio('Create', "RD1", key = '1')],
            [sg.Radio('Read', "RD1", key='2')],
            [sg.Radio('Delete', "RD1", key = '3')],
            [sg.Radio('List', "RD1", key='4')],
            [sg.Radio('Return', "RD1", key = '5')],
            [sg.Button('Confirmar'), sg.Cancel('Cancel')]
        ]
        self.__window = sg.Window('playerview').Layout(layout)