import os

class BetterView:

    def display_options(self):
        os.system('cls')
        print("============ CRUD Better ============")
        print('1) CREATE')
        print('2) READ')
        print('3) UPDATE')
        print('4) DELETE')
        print('5) LIST')
        print('6) Return')

        while True:
            try:
                option = int(input('>>> '))
                if option in (1,2,3,4,5,6):
                    return option
                else: 
                    print("Let's Try again, shall we?")
            except:
                raise Exception('C\'mon... Gimme some real numbers')
    
    def get_better_info(self):
        os.system('cls')
        print()
        print('Inform the better data:')
        name = input('Name:')
        nick = input('Nick:')
        wallet = input('Funds:')
        cpf = input('CPF:')
        return {'name': name, 'nick': nick, 'wallet': wallet, 'cpf': cpf}
    
    def get_by_id(self):
        print('Inform the ID:')
        id = input(id)
        return id
    
    def display_message(message):
        print(message)
    
    def clear_screen():
        os.system('cls')