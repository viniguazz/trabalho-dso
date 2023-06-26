import PySimpleGUI as sg
from view.abstract_view import AbstractView
from exception import NoMenuSelected, EmptyInputException, CancelOperationException

class PlayerView(AbstractView):
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
        try:
            button, values = self.open()
            
            if button in (None, 'Cancelar'):
                raise CancelOperationException
            if any in values is None:
                raise EmptyInputException
            name = values['name']
            victories = int(values['victories'])
            losses = int(values['losses'])
            draws = int(values['draws'])
        
            self.close()
            return {'name': name, 'victories': victories, 'losses': losses, 'draws': draws}
        
        except (CancelOperationException) as e:
            self.display_message(e)
            self.close()
            return None
        except (EmptyInputException) as e:
            self.display_message(e)
            self.close()
            return self.get_player_info()
        except:
            self.close()
            self.display_message("Please insert valid types")
            return self.get_player_info()
        
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
            [sg.Text('"============ CRUD PLAYER ============')],
            [sg.Radio('Create', "RD1", key = '1')],
            [sg.Radio('Read', "RD1", key='2')],
            [sg.Radio('Update', "RD1", key = '3')],
            [sg.Radio('Delete', "RD1", key = '4')],
            [sg.Radio('List', "RD1", key='5')],
            [sg.Radio('Return', "RD1", key = '6')],
            [sg.Button('Confirmar'), sg.Cancel('Cancel')]
        ]
        self.__window = sg.Window('playerview').Layout(layout)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values