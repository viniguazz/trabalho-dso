# Luan
#Como a classe sport não existe foi trocado por um string
#isTraded foi retirado por não termos mais marketplace
#Como é xadrez 1x1 foi retirado n_contestant por enquanto e sport
#Sentiu-se a necessidade de criar uma classe chamada Result
#Ira analisar se fica melhor implementar o odds como dict ou como uma classe própria

class Game():
    def __init__(self, id : int, odds : dict, bets : bets, status : bool, aceept_bet : bool, n_contestant : int):
        if not isinstance(id, int):
            raise
        if not isinstance(odds, ):
            raise
        if not isinstance(status, bool):
            raise
        
        
        #Atributos inicializados vazios 
        self.__pool = float()
        self.__result = bool()
        self.__odds = Odds()
    