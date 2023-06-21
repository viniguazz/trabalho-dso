from view.abstract_view import AbstractView
import PySimpleGUI as sg

class AdminView(AbstractView):
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
        if values['5'] or button in (None,'Cancelar'):
            opcao = 5
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
            [sg.Button('Submit'), sg.Cancel('Cancel')]
        ]
        self.__window = sg.Window('adminview').Layout(layout)
        
    def close(self):
        self.__window.Close()
    
    def open(self):
        button, values = self.__window.Read()
        return button, values