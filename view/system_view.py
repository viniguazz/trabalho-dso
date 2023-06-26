from view import AbstractView
import PySimpleGUI as sg
from exception import NoMenuSelected


class SystemView(AbstractView):

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

    def close(self):
        self.__window.Close()

    def init_components(self):
        sg.ChangeLookAndFeel('BlueMono')
        layout = [
            [sg.Text('====================== HELL BETS ======================')],
            [sg.Text('Choose your destiny:')],
            [sg.Radio('View Current Games', "RD1", key = '1')],
            [sg.Radio('Place Bet', "RD1", key='2')],
            [sg.Radio('Check Bets and Balance', "RD1", key = '3')],
            [sg.Radio('Admin', "RD1", key = '4')],
            [sg.Radio('Exit', "RD1", key='5')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('systemview').Layout(layout)