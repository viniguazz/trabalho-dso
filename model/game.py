from model.player import Player
from model.odds import Odds
from model.result import Result
from model.tipo_errado_exception import TipoErradoException

class Game():
    def __init__(self,id : int, name : str, player1 : Player, player2 : Player):

        if not isinstance(name, str):
            raise TipoErradoException

        if not isinstance(player1 , Player):
            raise TipoErradoException

        if not isinstance(player2 , Player):
            raise TipoErradoException
        
        self.__id = id
        self.__player1 = player1
        self.__player2 = player2
        # self.__pool_draw = 0.0
        # self.__pool_vict1 = 0.0
        # self.__pool_vict2 = 0.0
        self.__result = None
        self.__odds = None
        self.__bets = []
        self.__name = name

    @property
    def id(self):
        return self.__id
        
    @property
    def odds(self):
        return self.__odds
    
    # @property
    # def pool_draw(self):
    #     return self.__pool_draw
    
    # @property
    # def pool_vict1(self):
    #     return self.__pool_vict1
    
    # @property
    # def pool_vict2(self):
    #     return self.__pool_vict2

    @property
    def bets(self):
        return self.__bets

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def player1(self):
        return self.__player1

    @player1.setter
    def player1(self, player1):
        self.__player1 = player1
        
    @property
    def player2(self):
        return self.__player2

    @player2.setter
    def player2(self, player2):
        self.__player2 = player2

    @property
    def result(self):
        return self.__result

    @result.setter
    def result(self, result):
        if not (isinstance(result, Result)):
            raise TipoErradoException
        self.__result = result
        self.encerrar_jogo()
        
    def add_bet(self, bet):
        from model.bet import Bet
        if not (isinstance(bet, Bet)):
            raise TipoErradoException
        self.__bets.append(bet)
        # self.update_pools()
        # self.update_odds()
        
    def remove_bet(self,bet):
        from model.bet import Bet
        if not (isinstance(bet,Bet)):
            raise TipoErradoException
        self.__bets.remove(bet)
        # self.update_pools()
        # self.update_odds()
        
    # def update_pools(self):
    #     self.__pool_draw = 0.0
    #     self.__pool_vict1 = 0.0
    #     self.__pool_vict2 = 0.0
    #     for i in self.__bets:
    #         if i.result.outcome == "Draw":
    #             self.__pool_draw += i.price
    #         else:
    #             if i.result.player == self.__player1:
    #                 self.__pool_vict1 += i.price
    #             else:
    #                 self.__pool_vict2 += i.price
    
    # def update_odds(self):
    #     self.odds = Odds(self.__player1, self.__player2, 
    #                      self.__pool_vict1, self.__pool_vict2, 
    #                      self.__pool_draw)
        
#Testar qual versão funciona

    def encerrar_jogo(self):             
        for bet in self.__bets:
            bet.__status(False)
            if bet.__result == self.__result:
                bet.__better.__add_money((bet.__price + bet.__price*bet.__odd))

    # def encerrar_jogo(self):             
    #     for bet in self.__bets:
    #         bet.__status(False)
    #         if bet.result() == self.__result:
    #             bet.better().add_money((bet.price() + bet.price()*bet.odd()))