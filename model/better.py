# Luan

from model.person import Person
from model.tipo_errado_exception import TipoErradoException

# is_premium foi retirado pois estava envolvido com o marketplace, que não sera mais implementado
# wallet, foi reduzido de escopo de objeto para um simples float por enquanto ?
# Para clareza de leitura em add_funds e remove_funds funds foi substituido por money

class Better(Person):
    def __init__(self, name : str, id: int, nick : 
                str, wallet : float, cpf: str):
        if not isinstance(nick, str):
            raise TipoErradoException
        if not isinstance(wallet,float):
            raise TipoErradoException
        if not isinstance(cpf, str):
            raise TipoErradoException
        if not isinstance(wallet, float):
            raise TipoErradoException
        super().__init__(self, name, id)        
        self.__bets = []
        self.__wallet = wallet
        self.__nick = nick
        self.__cpf = cpf
    
    @property
    def nick(self):
        return self.__nick

    @nick.setter
    def nick(self, nick):
        self.__nick =nick
    
    @property
    def wallet(self):
        return self.__wallet
    
    @property
    def bets(self):
        return self.__bets
    
    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf
        
    def add_money(self, add):
        self.__wallet += add
    
    def remove_money(self, remove):
        self.__wallet -= remove

    def add_bet(self, bet):
        from model.bet import Bet
        if not isinstance(bet, Bet):
            raise TipoErradoException
        if bet not in self.__bets:
            self.__bets.append(bet)
        else:
            print("Bet já presente")
            
    def remove_bet(self, bet):
        from model.bet import Bet
        if not isinstance(bet, Bet):
            raise TipoErradoException
        if bet in self.__bets:
            self.__bets.remove(bet)
        else:
            print("Bet não existe")