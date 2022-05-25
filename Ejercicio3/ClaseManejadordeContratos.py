import imp
from ClaseContrato import Contrato
import numpy

class ManejadorDeContratos:
    __ArregloContratos = None
    __CantidadDeContratos = 0
    __Incremento = 5
    __dimesion = 5

    def __init__(self,dimension = 5):
        self.__dimesion = dimension
        self.__ArregloContratos = numpy.empty(dimension, dtype=Contrato)
        self.__CantidadDeContratos = 0
        self.__Incremento = 5
        
    
    def CrearContrato(self, aniodeinicio, mesdeinicio, diadeinicio, aniodefin,mesdefin,diadefin,costoMesual, jugador,equipo):
        if self.__CantidadDeContratos == len(self.__ArregloContratos):
            self.__dimesion += self.__Incremento
            self.__ArregloContratos.resize(self.__dimesion)
        self.__ArregloContratos[self.__CantidadDeContratos] = Contrato(aniodeinicio,mesdeinicio,diadeinicio,aniodefin,mesdefin,diadefin,costoMesual, jugador,equipo)
        jugador.agregarContrato(self.__ArregloContratos[self.__CantidadDeContratos])
        equipo.agregarContrato(self.__ArregloContratos[self.__CantidadDeContratos])
        self.__CantidadDeContratos += 1
    
    def MostrarContratos(self):
        for i in range(len(self.__ArregloContratos)):
            print(self.__ArregloContratos[i])