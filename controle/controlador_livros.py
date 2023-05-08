from limite.tela_livro import TelaLivro
from entidade.livro import Livro

class ControladorLivros():

  # Fazer lançamento e tratamento de exceções, ao invés de apenas mostrar mensagem na tela.
  def __init__(self, controlador_sistema):
    self.__livros = []
    self.__controlador_sistema = controlador_sistema
    self.__tela_livro = TelaLivro()

  def pega_livro_por_codigo(self, codigo: int):
    for livro in self.__livros:
      if(livro.codigo == codigo):
        return livro
    return None

  def incluir_livro(self):
    dados_livro = self.__tela_livro.pega_dados_livro()
    l = self.pega_livro_por_codigo(dados_livro["codigo"])
    if l is None:
      livro = Livro(dados_livro["titulo"], dados_livro["codigo"])
      self.__livros.append(livro)
    else:
      self.__tela_livro.mostra_mensagem("ATENCAO: Livro já existente")

  def alterar_livro(self):
    self.lista_livro()
    codigo_livro = self.__tela_livro.seleciona_livro()
    livro = self.pega_livro_por_codigo(codigo_livro)

    if(livro is not None):
      novos_dados_livro = self.__tela_livro.pega_dados_livro()
      livro.titulo = novos_dados_livro["titulo"]
      livro.codigo = novos_dados_livro["codigo"]
      self.lista_livro()
    else:
      self.__tela_livro.mostra_mensagem("ATENCAO: Livro não existente")

  # Sugestão: se a lista estiver vazia, mostrar a mensagem de lista vazia
  def lista_livro(self):
    for livro in self.__livros:
      self.__tela_livro.mostra_livro({"titulo": livro.titulo, "codigo": livro.codigo})

  def excluir_livro(self):
    self.lista_livro()
    codigo_livro = self.__tela_livro.seleciona_livro()
    livro = self.pega_livro_por_codigo(codigo_livro)

    if(livro is not None):
      self.__livros.remove(livro)
      self.lista_livro()
    else:
      self.__tela_livro.mostra_mensagem("ATENCAO: Livro não existente")

  def retornar(self):
    self.__controlador_sistema.abre_tela()

  def abre_tela(self):
    lista_opcoes = {1: self.incluir_livro, 2: self.alterar_livro, 3: self.lista_livro, 4: self.excluir_livro, 0: self.retornar}

    continua = True
    while continua:
      lista_opcoes[self.__tela_livro.tela_opcoes()]()