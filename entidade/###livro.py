class Livro:
  # fazer aqui tratamento dos dados, caso os parametros sejam diferentes do esperado
  def __init__(self, titulo: str, codigo: int):
    self.__titulo = titulo
    self.__codigo = codigo

  @property
  def titulo(self):
    return self.__titulo

  @titulo.setter
  def titulo(self, titulo):
    self.__titulo = titulo

  @property
  def codigo(self):
    return self.__codigo

  @codigo.setter
  def codigo(self, codigo):
    self.__codigo = codigo