from ClaseCalefactor import Calefactor

class CalefactorElectrico(Calefactor):
    __potenciaMaxima = int

    def __init__(self, marca, modelo, potenciaMaxima):
        super().__init__(marca, modelo)
        self.__potenciaMaxima = int(potenciaMaxima)
    
    def getPotencia(self):
        return self.__potenciaMaxima
    
    def __str__(self):
        return super().__str__() + "Potencia Maxima: {}".format(self.__potenciaMaxima)