class contadoresFlor:
    __contador = 0
    __codigo  = 0

    def __init__(self, contador, codigo ):
        self.__contador = contador
        self.__codigo = codigo
    
    def __gt__(self,otro):
        if type(otro) == contadoresFlor:
            return otro.getContador() > self.__contador
    
    def getContador(self):
        return self.__contador
    
    def sumarContador(self):
        self.__contador+=1
    
    def getCodigo(self):
        return self.__codigo