import csv
import numpy
from ClaseFlores import Flor

class ManejadorDeFlores:
    __ArregloFlores = None
    __CantidadDeFlores = 9
    def __init__(self):
        self.__ArregloFlores = numpy.empty(self.__CantidadDeFlores, dtype= Flor)
    
    def Carga(self):
        archivo = open("c:\\Users\\Usuario\\Desktop\\POO\\Unidad-3\\Ejercicio2\\flores.csv")
        reader = csv.reader(archivo, delimiter=",")

        i = 0
        for files in reader:
            UnaFlor = Flor(files[0],files[1],files[2],files[3])
            self.__ArregloFlores[i] = UnaFlor
            i+=1
        archivo.close
    
    def getFlorPorCodigo(self,codigo):
        return self.__ArregloFlores[codigo]
    
    def getTotalFlores(self):
        return self.__CantidadDeFlores