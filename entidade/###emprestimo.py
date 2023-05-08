from entidade.amigo import Amigo
from entidade.livro import Livro


class Emprestimo:
  def __init__(self, amigo: Amigo, livro: Livro, codigo: int):
    if (isinstance(livro, Livro)):
        self.__livro = livro
    if (isinstance(amigo, Amigo)):
        self.__amigo = amigo

    self.__codigo = codigo

  @property
  def amigo(self):
    return self.__amigo

  @property
  def livro(self):
    return self.__livro

  @property
  def codigo(self):
    return self.__codigo

  @amigo.setter
  def amigo(self, amigo: Amigo):
    if (isinstance(amigo, Amigo)):
        self.__amigo = amigo

  @livro.setter
  def livro(self, livro: Livro):
    if (isinstance(livro, Livro)):
        self.__livro = livro

  @codigo.setter
  def codigo(self, codigo: int):
    self.__codigo = codigo