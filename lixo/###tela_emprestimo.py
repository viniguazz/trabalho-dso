class TelaEmprestimo():
  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def tela_opcoes(self):
    print("-------- EMPRESTIMOS ----------")
    print("Escolha a opcao")
    print("1 - Fazer Emprestimo")
    print("2 - Listar Emprestimos")
    print("3 - Devolver Emprestimo")
    print("0 - Retornar")

    opcao = int(input("Escolha a opcao: "))
    return opcao

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def pega_dados_emprestimo(self):
    print("-------- DADOS EMPRESTIMO ----------")
    cpf = input("CPF Amigo: ")
    codigo = input("Codigo Livro: ")

    return {"cpf": cpf, "codigo": codigo}

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def mostra_emprestimo(self, dados_emprestimo):
    print("CODIGO DO EMPRESTIMO: ", dados_emprestimo["codigo"])
    print("TITULO DO LIVRO: ", dados_emprestimo["titulo_livro"])
    print("CODIGO DO LIVRO: ", dados_emprestimo["codigo_livro"])
    print("NOME DO AMIGO: ", dados_emprestimo["nome_amigo"])
    print("CPF DO AMIGO: ", dados_emprestimo["cpf_amigo"])
    print("\n")

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def seleciona_emprestimo(self):
    codigo = input("Código do emprestimo que deseja selecionar: ")
    return codigo

  def mostra_mensagem(self, msg):
    print(msg)