from limite.tela_amigo import TelaAmigo
from entidade.amigo import Amigo

class ControladorAmigos():

  def __init__(self, controlador_sistema):
    self.__amigos = []
    self.__tela_amigo = TelaAmigo()
    self.__controlador_sistema = controlador_sistema

  def pega_amigo_por_cpf(self, cpf: int):
    for amigo in self.__amigos:
      if(amigo.cpf == cpf):
        return amigo
    return None

  # Sugestão: não deixe cadastrar dois amigos com o mesmo CPF
  def incluir_amigo(self):
    dados_amigo = self.__tela_amigo.pega_dados_amigo()
    amigo = Amigo(dados_amigo["nome"], dados_amigo["telefone"], dados_amigo["cpf"])
    self.__amigos.append(amigo)

  def alterar_amigo(self):
    self.lista_amigos()
    cpf_amigo = self.__tela_amigo.seleciona_amigo()
    amigo = self.pega_amigo_por_cpf(cpf_amigo)

    if(amigo is not None):
      novos_dados_amigo = self.__tela_amigo.pega_dados_amigo()
      amigo.nome = novos_dados_amigo["nome"]
      amigo.telefone = novos_dados_amigo["telefone"]
      amigo.cpf = novos_dados_amigo["cpf"]
      self.lista_amigos()
    else:
      self.__tela_amigo.mostra_mensagem("ATENCAO: Amigo não existente")

  # Sugestão: se a lista estiver vazia, mostrar a mensagem de lista vazia
  def lista_amigos(self):
    for amigo in self.__amigos:
      self.__tela_amigo.mostra_amigo({"nome": amigo.nome, "telefone": amigo.telefone, "cpf": amigo.cpf})

  def excluir_amigo(self):
    self.lista_amigos()
    cpf_amigo = self.__tela_amigo.seleciona_amigo()
    amigo = self.pega_amigo_por_cpf(cpf_amigo)

    if(amigo is not None):
      self.__amigos.remove(amigo)
      self.lista_amigos()
    else:
      self.__tela_amigo.mostra_mensagem("ATENCAO: Amigo não existente")

  def retornar(self):
    self.__controlador_sistema.abre_tela()

  def abre_tela(self):
    lista_opcoes = {1: self.incluir_amigo, 2: self.alterar_amigo, 3: self.lista_amigos, 4: self.excluir_amigo, 0: self.retornar}

    continua = True
    while continua:
      lista_opcoes[self.__tela_amigo.tela_opcoes()]()