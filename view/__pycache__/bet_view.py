import PySimpleGUI as sg
from view.abstract_view import AbstractView

class BetView(AbstractView):
    def __init__(self):
        super().__init__()

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values

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
        if values['5']  or button in (None, 'Cancelar'):
            opcao = 5
        self.close()
        return opcao

    def display_add_bet(self):
        layout = [
            [sg.Text('"============ TIME TO LOSE MONEY! ============')],
            [sg.Radio('Place bet', "RD1", key = '1')],
            [sg.Radio('Return', "RD1", key='2')],
            [sg.Button('Submit'), sg.Cancel('Cancel')]
        ]
        self.__window = sg.Window('displayaddbet').Layout(layout)

        button, values = self.open()
        if values['1']:
            option = 1
        else:
            option = 2
        self.close()
        return int(option)

    def display_stats(self):
        layout = [
            [sg.Text('"============ STATS ============')],
            [sg.Radio('Check bets and funds', "RD1", key = '1')],
            [sg.Radio('Return', "RD1", key='2')],
            [sg.Button('Submit'), sg.Cancel('Cancel')]
        ]
        self.__window = sg.Window('displaystats').Layout(layout)

        button, values = self.open()
        if values['1']:
            option = 1
        else:
            option = 2
        self.close()
        return int(option)
    
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
                return
            game_id = int(values['game_id'])
            price = float(values['price'])
            if values['2']:
                result = {'outcome:' : 'Draw', 'player' : None}
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
        except:
            self.close()
            self.display_message("Please insert valid types")
            self.get_bet_info()


    def get_by_id(self):
        layout = [
            [sg.Text('Inform the ID:')],
            [sg.Text('ID:'), sg.InputText('', key ='id')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('getbyid').Layout(layout)
        try:
            button, values = self.open()
            id = values['id']
            self.close()
            return int(id)
        except:
            self.close()
            self.display_message("Please insert valid types")
            self.get_by_id()

    def list_bets(self, bets):
        string_bets = ""
        for bet in bets:
            if bet.result.outcome == 'Draw':
                string_bets = string_bets + "BetterId" + str(bet.better.name) +'\n'
                string_bets = string_bets + "Price: " + str(bet.price) +'\n'
                string_bets = string_bets + "Game: " + str(bet.game.name) +'\n'
                string_bets = string_bets + "Result: " + str(bet.result.outcome) +'\n'
                string_bets = string_bets + "Odd: " + str(bet.odd) +'\n'
            else:
                string_bets = string_bets + "BetterId" + str(bet.better.name) +'\n'
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
            [sg.Button('Submit'), sg.Cancel('Cancel')]
        ]
        self.__window = sg.Window('playerview').Layout(layout)