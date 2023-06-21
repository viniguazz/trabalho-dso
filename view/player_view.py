import PySimpleGUI as sg
from view.abstract_view import AbstractView

class PlayerView(AbstractView):
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
    
    def get_player_info(self):
        layout = [
            [sg.Text('Inform the PLAYER data:')],
            [sg.Text('Name:'), sg.InputText('', key = 'name')],
            [sg.Text('Victories:'), sg.InputText('', key = 'victories')],
            [sg.Text('Losses:'), sg.InputText('', key = 'losses')],
            [sg.Text('Draws:'), sg.InputText('', key = 'draws')],
            [sg.Button('Confirmar') , sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('getplayerinfo').Layout(layout)

        button, values = self.open()
        name = values['name']
        victories = int(values['victories'])
        losses = int(values['losses'])
        draws = int(values['draws'])

        self.close()
        return {'name': name, 'victories': victories, 'losses': losses, 'draws': draws}
        
    def list_players(self, players):
        string_all_players = ""
        for player in players:
            string_all_players = string_all_players + "ID: " + str(player.id) +'\n'
            string_all_players = string_all_players + "Name: " + player.name +'\n'
            string_all_players = string_all_players + "Victories: " + str(player.stats.victories) +'\n'
            string_all_players = string_all_players + "Losses: " + str(player.stats.losses) +'\n'
            string_all_players = string_all_players + "Draws: " + str(player.stats.draws) +'\n'
        sg.Popup('============ LIST PLAYERS ============', string_all_players)

    def get_by_id(self):
        layout = [
            [sg.Text('Inform the ID:')],
            [sg.Text('ID:'), sg.InputText('', key ='id')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('getplayerid').Layout(layout)

        button, values = self.open()
        id = values['id']
        self.close()
        return int(id)

    def init_components(self):
        layout = [
            [sg.Text('"============ CRUD PLAYER ============')],
            [sg.Radio('Create', "RD1", key = '1')],
            [sg.Radio('Read', "RD1", key='2')],
            [sg.Radio('Update', "RD1", key = '3')],
            [sg.Radio('Delete', "RD1", key = '4')],
            [sg.Radio('List', "RD1", key='5')],
            [sg.Radio('Return', "RD1", key = '6')],
            [sg.Button('Submit'), sg.Cancel('Cancel')]
        ]
        self.__window = sg.Window('playerview').Layout(layout)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values