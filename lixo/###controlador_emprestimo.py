from limite.tela_emprestimo import TelaEmprestimo
from entidade.emprestimo import Emprestimo

from random import randint


# Fazer lançamento e tratamento de exceções, ao invés de apenas mostrar mensagem na tela.
class ControladorEmprestimos():

  def __init__(self, controlador_sistema):
    self.__controlador_sistema = controlador_sistema
    self.__emprestimos = []
    self.__tela_emprestimo = TelaEmprestimo()

  def pega_emprestimo_por_codigo(self, codigo: int):
    for emprestimo in self.__emprestimos:
      if(emprestimo.codigo == codigo):
        return emprestimo
    return None

  #Sugestao: listar apenas os livros que não estão emprestados
  def incluir_emprestimo(self):
    self.__controlador_sistema.controlador_amigos.lista_amigos()
    self.__controlador_sistema.controlador_livros.lista_livro()
    dados_emprestimo = self.__tela_emprestimo.pega_dados_emprestimo()

    amigo = self.__controlador_sistema.controlador_amigos.pega_amigo_por_cpf(dados_emprestimo["cpf"])
    livro = self.__controlador_sistema.controlador_livros.pega_livro_por_codigo(dados_emprestimo["codigo"])
    if (amigo is not None and livro is not None):
      emprestimo = Emprestimo(amigo, livro, randint(0, 100))
      self.__emprestimos.append(emprestimo)
    else:
      self.__tela_emprestimo.mostra_mensagem("Dados invalidos")

  #Sugestão: se a lista estiver vazia, mostrar a mensagem de lista vazia
  def lista_emprestimo(self):
    for e in self.__emprestimos:
      self.__tela_emprestimo.mostra_emprestimo({"codigo": e.codigo,
                                                "titulo_livro": e.livro.titulo,
                                                "codigo_livro": e.livro.codigo,
                                                "nome_amigo": e.amigo.nome,
                                                "cpf_amigo": e.amigo.cpf})

  def excluir_emprestimo(self):
    self.lista_emprestimo()
    codigo_emprestimo = self.__tela_emprestimo.seleciona_emprestimo()
    emprestimo = self.pega_emprestimo_por_codigo(int(codigo_emprestimo))

    if (emprestimo is not None):
      self.__emprestimos.remove(emprestimo)
      self.lista_emprestimo()
    else:
      self.__tela_emprestimo.mostra_mensagem("ATENCAO: Emprestimo não existente")

  def retornar(self):
    self.__controlador_sistema.abre_tela()

  def abre_tela(self):
    lista_opcoes = {1: self.incluir_emprestimo, 2: self.lista_emprestimo, 3: self.excluir_emprestimo,0: self.retornar}

    continua = True
    while continua:
      lista_opcoes[self.__tela_emprestimo.tela_opcoes()]()
