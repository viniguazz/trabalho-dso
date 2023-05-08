class TelaLivro():
  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def tela_opcoes(self):
    print("-------- LIVROS ----------")
    print("Escolha a opcao")
    print("1 - Incluir Livro")
    print("2 - Alterar Livro")
    print("3 - Listar Livro")
    print("4 - Excluir Livro")
    print("0 - Retornar")

    opcao = int(input("Escolha a opcao: "))
    return opcao

  #fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def pega_dados_livro(self):
    print("-------- DADOS LIVRO ----------")
    titulo = input("Titulo: ")
    codigo = input("Codigo: ")

    return {"titulo": titulo, "codigo": codigo}

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def mostra_livro(self, dados_livro):
    print("TITULO DO LIVRO: ", dados_livro["titulo"])
    print("CODIGO DO LIVRO: ", dados_livro["codigo"])
    print("\n")

  #fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def seleciona_livro(self):
    codigo = input("Código do livro que deseja selecionar: ")
    return codigo

  def mostra_mensagem(self, msg):
    print(msg)