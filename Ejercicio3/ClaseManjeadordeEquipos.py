from csv import reader
import csv
from ClaseEquipo import Equipo
import numpy

class ManejadorDeEquipos:
    __arregloEquipos = None

    def __init__(self):
        archivo = open("c:\\Users\\Usuario\\Desktop\\POO\\Unidad-3\\Ejercicio3\\Equipos.csv")
        reader = csv.reader(archivo, delimiter=";")
        self.__arregloEquipos = numpy.empty(int(next(reader)[0]), dtype= Equipo)
        archivo.close
        
    
    def Carga(self):
        archivo = open("c:\\Users\\Usuario\\Desktop\\POO\\Unidad-3\\Ejercicio3\\Equipos.csv")
        reader = csv.reader(archivo, delimiter=";")

        bandera = False
        i = 0
        for files in reader:
            if bandera == False:
                bandera = True
            else:
                UnEquipo = Equipo(files[0],files[1])
                self.__arregloEquipos[i] = UnEquipo
                i+=1
        
        archivo.close

    def getEquipo(self,nombre):
        equipoADevolver = None
        for i in range(len(self.__arregloEquipos)):
            if self.__arregloEquipos[i].getNombre() == nombre:
                equipoADevolver = self.__arregloEquipos[i]
        return equipoADevolver

    def getBoca(self):
        contratos = self.__arregloEquipos[0].getContratos()
        for i in range(len(contratos)):
            print(contratos[i])