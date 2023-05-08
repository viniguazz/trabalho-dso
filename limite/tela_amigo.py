
class TelaAmigo():
  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def tela_opcoes(self):
    print("-------- AMIGOS ----------")
    print("Escolha a opcao")
    print("1 - Incluir Amigo")
    print("2 - Alterar Amigo")
    print("3 - Listar Amigos")
    print("4 - Excluir Amigo")
    print("0 - Retornar")

    opcao = int(input("Escolha a opcao: "))
    return opcao

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def pega_dados_amigo(self):
    print("-------- DADOS AMIGO ----------")
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    cpf = input("CPF: ")

    return {"nome": nome, "telefone": telefone, "cpf": cpf}

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def mostra_amigo(self, dados_amigo):
    print("NOME DO AMIGO: ", dados_amigo["nome"])
    print("FONE DO AMIGO: ", dados_amigo["telefone"])
    print("CPF DO AMIGO: ", dados_amigo["cpf"])
    print("\n")

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def seleciona_amigo(self):
    cpf = input("CPF do amigo que deseja selecionar: ")
    return cpf

  def mostra_mensagem(self, msg):
    print(msg)