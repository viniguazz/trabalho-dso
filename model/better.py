from model import Person
from exception import InvalidNativeTypeException, InvalidPlayerException, InvalidBetException

        
class Better(Person):

    def __init__(self, id: int , name : str, nick : 
                str, wallet : float, cpf: str):

        if not isinstance(nick, str):
            raise InvalidNativeTypeException(nick, "str")

        if not isinstance(wallet,float):
            raise InvalidNativeTypeException(wallet, "float")

        if not isinstance(cpf, str):
            raise InvalidNativeTypeException(cpf, "str")

        if not isinstance(wallet, float):
            raise InvalidNativeTypeException(wallet, "float")

        super().__init__(name)

        self.__id = id
        self.__wallet = wallet
        self.__nick = nick
        self.__cpf = cpf
        self.__bets = []
    
    @property
    def nick(self):
        return self.__nick
    
    @property
    def id(self):
        return self.__id

    @property
    def bets(self):
        return self.__bets

    @property
    def wallet(self):
        return self.__wallet

    @property
    def bets(self):
        return self.__bets
    
    @property
    def cpf(self):
        return self.__cpf
    
    @id.setter
    def id(self, id):
        self.__id = id

    @nick.setter
    def nick(self, nick):
        self.__nick =nick
    
    @wallet.setter
    def wallet(self, wallet):
        self.__wallet = wallet
    
    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    def add_bet(self, bet):
        if isinstance(bet, bet):
            self.__bets.append(bet)
            return bet
        raise InvalidBetException(bet)
        
    def add_money(self, add):
        self.__wallet += add
    
    def remove_money(self, remove):
        self.__wallet -= remove