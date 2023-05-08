
class Amigo:
  # fazer aqui tratamento dos dados, caso os parametros sejam diferentes do esperado
  def __init__(self, nome: str, telefone: str, cpf: int):
    self.__nome = nome
    self.__telefone = telefone
    self.__cpf = cpf

  @property
  def nome(self):
    return self.__nome

  @property
  def telefone(self):
    return self.__telefone

  @property
  def cpf(self):
    return self.__cpf

  @nome.setter
  def nome(self, nome: str):
    self.__nome = nome

  @telefone.setter
  def telefone(self, telefone: str):
    self.__telefone = telefone

  @cpf.setter
  def cpf(self, cpf: str):
    self.__cpf = cpf
