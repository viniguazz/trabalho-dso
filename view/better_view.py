import PySimpleGUI as sg
from view.abstract_view import AbstractView

class BetterView(AbstractView):
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
    
    def get_better_info(self):
        layout = [
            [sg.Text('Inform the Better data:')],
            [sg.Text('Name:'), sg.InputText('', key = 'name')],
            [sg.Text('Nick:'), sg.InputText('', key = 'nick')],
            [sg.Text('Funds:'), sg.InputText('', key = 'funds')],
            [sg.Text('CPF:'), sg.InputText('', key = 'cpf')],
        ]
        self.__window = sg.Window('getbetterinfo').Layout(layout)

        button, values = self.open()
        name = values['name']
        nick = values['nick']
        wallet = float(values['funds'])
        cpf = values['cpf']

        self.close()
        return {'name': name, 'nick': nick, 'wallet': wallet, 'cpf': cpf}
    
    def get_by_id(self):
        layout = [
            [sg.Text('Inform the ID:')],
            [sg.Text('ID:'), sg.InputText('', key ='id')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('getbetterid').Layout(layout)

        button, values = self.open()
        id = values['id']
        self.close()
        return int(id)
    
    def init_components(self):
        layout = [
            [sg.Text('"============ CRUD Better ============')],
            [sg.Radio('Create', "RD1", key = '1')],
            [sg.Radio('Read', "RD1", key='2')],
            [sg.Radio('Update', "RD1", key = '3')],
            [sg.Radio('Delete', "RD1", key = '4')],
            [sg.Radio('List', "RD1", key='5')],
            [sg.Radio('Return', "RD1", key = '6')],
            [sg.Button('Submit'), sg.Cancel('Cancel')]
        ]
        self.__window = sg.Window('betterview').Layout(layout)
    
    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values
    
    def list_better(self, betters):
        string_betters = ""
        for better in betters:

            string_betters = string_betters + "Id" + str(better.id) +'\n'
            string_betters = string_betters + "Name: " + str(better.name) +'\n'
            string_betters = string_betters + "Nick: " + str(better.nick) +'\n'
            string_betters = string_betters + "Wallet: " + str(better.wallet) +'\n'
            string_betters = string_betters + "CPF: " + str(better.cpf) +'\n'

        sg.Popup('============ LIST BETTER ============', string_betters)
    
    
    def display_better_data(self, better):
        string_bets = ""
        string_bets = string_bets + "Better Name: " + better.name +'\n'
        for bet in better["bets"]:
            string_bets = string_bets + "Bet Id: " + str(bet.id) +'\n'
            string_bets = string_bets + "Price: " + str(bet.price) +'\n'
            string_bets = string_bets + "Game: " + str(bet.game.name) +'\n'
        if bet.result.outcome == 'Draw':
            string_bets = string_bets + "Outcome: " + str(bet.result.outcome) +'\n'
        else:
            string_bets = string_bets + "Outcome: " + str(bet.result.outcome) +'\n'
            string_bets = string_bets + "Player: " + str(bet.result.player.name) +'\n'    
        string_bets = string_bets + 'Balance' + str(better["wallet"])
        sg.Popup('============ LIST BETS OF BETTER ============', string_bets)