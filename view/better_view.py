import os

class BetterView:

    def display_options(self):
        print("============ STATS ============")
        print("1) Check bets and Funds")
        print("2) Return")
        while True:
            try:
                option = int(input())
                return option
            except:
                raise Exception('f*** off. gimme some real f******* numbers')
    
    def get_better_info(self):
        os.system('cls')
        print()
        print('Inform the better data:')
        name = input('Name:')
        nick = input('Nick:')
        wallet = input('Funds:')
        cpf = input('CPF:')
        return {'name': name, 'nick': nick, 'wallet': wallet, 'cpf': cpf}
    
    
    def get_better(self):
        os.system('cls')
        print()
        better_id = input('Inform the better\'s ID:')
        return better_id

    def display_better_data(self, better):
        os.system('cls')
        print()
        print('Bets')
        print()
        for bet in better["bets"]:
            print(f'| Price: {bet["price"]}   | Game: {bet["game"]}  | result: {bet["result"]}       ')
        print()
        print('Balance:')
        print()
        print(better['wallet'])
        print()
        input('Press any key to ')
