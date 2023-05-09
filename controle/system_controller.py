from system_view import SystemView
from game_list_controller import GameListController
from bet_controller import BetController
from user_controller import UserController

class SystemController:

    def __init__(self):
        self.__system_view = SystemView(self)
        self.__game_list_controller = GameListController(self)
        self.__bet_controller = BetController(self)
        self.__user_controller = UserController(self)

        self.__player_controller = PlayerController(self)
        self.__game_controller = GameController(self)
        
    @property
    def controlador_amigos(self):
        return self.__controlador_amigos

    @property
    def controlador_livros(self):
        return self.__controlador_livros

    def initialize_system(self):
        self.display_screen()
    
    def list_games(self):
        self.__game_list_controller.display_screen()

    def place_bet(self):
        self.__bet_controller.display_screen()

    def user_status(self):
        self.__user_controller.display_screen()



    def cadastra_livros(self):
        self.__controlador_livros.abre_tela()

    def cadastra_amigos(self):
        # Chama o controlador de Amigos
        self.__controlador_amigos.abre_tela()

    def cadastra_emprestimos(self):
        self.__controlador_emprestimos.abre_tela()
        # Chama o controlador de Emprestimos

    def encerra_sistema(self):
        exit(0)

    def display_screen(self):
        lista_opcoes = {1: self.cadastra_livros, 2: self.cadastra_amigos, 3: self.cadastra_emprestimos,
                        0: self.encerra_sistema}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()