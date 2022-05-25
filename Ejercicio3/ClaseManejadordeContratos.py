from csv import writer
import csv
import imp
from operator import le
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
            if self.__ArregloContratos[i] != None:
                print(self.__ArregloContratos[i])
    
    def getContratosVencimiento6(self, equipo):
        equipo = equipo.lower()
        for i in range(len(self.__ArregloContratos)):
            if self.__ArregloContratos[i] != None:
                MesesDeContrato =  self.__ArregloContratos[i].getDiferenciaMeses()
                
                if MesesDeContrato <= 6 and self.__ArregloContratos[i].getEquipo().getNombre().lower() == equipo:
                    print(self.__ArregloContratos[i].getJugador())
    
    def GuardarContratos(self):
        archivo = open('C:\\Users\\Usuario\\Desktop\\POO\\Unidad-3\\Ejercicio3\\Contratos.csv', 'w', newline='')
        writer = csv.writer(archivo)
        
        for i in range(len(self.__ArregloContratos)):
            if self.__ArregloContratos[i] != None:
                linea = [str(self.__ArregloContratos[i].getJugador().getDNI()),str(self.__ArregloContratos[i].getEquipo().getNombre()) , str(self.__ArregloContratos[i].getFechaInicio()),str(self.__ArregloContratos[i].getFechaFin()),str(self.__ArregloContratos[i].getCostoMensual())]
                writer.writerow(linea)
        archivo.close