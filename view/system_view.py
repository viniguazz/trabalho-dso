from view.abstract_view import AbstractView
import PySimpleGUI as sg

class SystemView(AbstractView):

    def __init__(self):
        self.__window = None
        self.init_components()


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
        # cobre os casos de voltar, não clicar em nada e fechar janela, ou clicar cancelar
        if values['5'] or button in (None,'Cancelar'):
            opcao = 5
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
            [sg.Button('Submit'), sg.Cancel('Cancel')]
        ]
        self.__window = sg.Window('systemview').Layout(layout)