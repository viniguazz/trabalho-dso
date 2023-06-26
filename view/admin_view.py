from view.abstract_view import AbstractView
import PySimpleGUI as sg
from exception import NoMenuSelected

class AdminView(AbstractView):
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
        elif values['5'] or button in (None, 'Cancelar'):
            opcao = 5
        elif button in ('Confirmar', None):
            raise NoMenuSelected
        self.close()
        return opcao

    def login(self):
        layout =[[sg.Text('Please insert the master PASSWORD:'), sg.InputText('', key = 'password')],
                 [sg.Button('Confirmar'), sg.Cancel('Cancelar')]]
        self.__window = sg.Window('getlogin').Layout(layout)

        button,values = self.open()
        self.close()
        return values['password']
    
    def init_components(self):
        layout = [
            [sg.Text('============ ADMIN OPTIONS ============')],
            [sg.Radio('Games', "RD1", key = '1')],
            [sg.Radio('Players', "RD1", key='2')],
            [sg.Radio('Betters', "RD1", key = '3')],
            [sg.Radio('Bets', "RD1", key = '4')],
            [sg.Radio('Return', "RD1", key = '5')],
            [sg.Button('Confirmar'), sg.Cancel('Cancel')]
        ]
        self.__window = sg.Window('adminview').Layout(layout)
        
    def close(self):
        self.__window.Close()
    
    def open(self):
        button, values = self.__window.Read()
        return button, values