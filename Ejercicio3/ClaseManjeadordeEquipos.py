from csv import reader
import csv
from ClaseEquipo import Equipo
import numpy

class ManejadorDeEquipos:
    __arregloEquipos = None
    __cantidadDeEquipos = 4

    def __init__(self):
        self.__arregloEquipos = numpy.empty(self.__cantidadDeEquipos, dtype= Equipo)
    
    def Carga(self):
        archivo = open("Equipos.csv")
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

    
