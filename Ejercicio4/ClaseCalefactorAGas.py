from ClaseCalefactor import Calefactor

class CalefactorAGas(Calefactor):
    __matricula = str
    __calorias = int

    def __init__(self, marca, modelo,matricula,calorias):
        super().__init__(marca, modelo)
        self.__matricula = matricula
        self.__calorias = int(calorias)
    
    def getCalorias(self):
        return self.__calorias
    
    def __str__(self):
        return super().__str__() + "Matricula: {}, Calorias: {}".format(self.__matricula,self.__calorias)