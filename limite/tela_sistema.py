class TelaSistema:
    #fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def tela_opcoes(self):
        print("-------- SisLivros ---------")
        print("Escolha sua opcao")
        print("1 - Livros")
        print("2 - Amigos")
        print("3 - Emprestimos")
        print("0 - Finalizar sistema")
        opcao = int(input("Escolha a opcao:"))
        return opcao