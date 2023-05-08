from limite.tela_sistema import TelaSistema
from controle.controlador_amigos import ControladorAmigos
from controle.controlador_livros import ControladorLivros
from controle.controlador_emprestimo import ControladorEmprestimos

class ControladorSistema:

    def __init__(self):
        self.__controlador_livros = ControladorLivros(self)
        self.__controlador_amigos = ControladorAmigos(self)
        self.__controlador_emprestimos = ControladorEmprestimos(self)
        self.__tela_sistema = TelaSistema()

    @property
    def controlador_amigos(self):
        return self.__controlador_amigos

    @property
    def controlador_livros(self):
        return self.__controlador_livros

    def inicializa_sistema(self):
        self.abre_tela()

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

    def abre_tela(self):
        lista_opcoes = {1: self.cadastra_livros, 2: self.cadastra_amigos, 3: self.cadastra_emprestimos,
                        0: self.encerra_sistema}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()