from model.person import Person
from exception.tipo_errado_exception import TipoErradoException

        
class Better(Person):

    def __init__(self, id: int , name : str, nick : 
                str, wallet : float, cpf: str):
        if not isinstance(nick, str):
            raise TipoErradoException
        if not isinstance(wallet,float):
            raise TipoErradoException
        if not isinstance(cpf, str):
            raise TipoErradoException
        if not isinstance(wallet, float):
            raise TipoErradoException
        super().__init__(name)        
        self.__id = id
        self.__wallet = wallet
        self.__nick = nick
        self.__cpf = cpf
    
    @property
    def nick(self):
        return self.__nick
    
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, id):
        self.__id = id

    @nick.setter
    def nick(self, nick):
        self.__nick =nick
    
    @property
    def wallet(self):
        return self.__wallet
    
    @wallet.setter
    def wallet(self, wallet):
        self.__wallet = wallet
    
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