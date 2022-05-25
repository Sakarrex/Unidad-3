from csv import reader
import csv
from tkinter.tix import Tree
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
        nombre = nombre.lower()
        equipoADevolver = None
        for i in range(len(self.__arregloEquipos)):
            if self.__arregloEquipos[i].getNombre().lower() == nombre:
                equipoADevolver = self.__arregloEquipos[i]
        return equipoADevolver

    def getImporteTotal(self,nombre):
        Total = 0
        nombre = nombre.lower()
        bandera = False
        i = 0
        EquipoAListar = None
        while i < len(self.__arregloEquipos) and bandera == False:
            if self.__arregloEquipos[i].getNombre().lower() == nombre:
                EquipoAListar = self.__arregloEquipos[i]
                bandera = True
            i+=1
        if EquipoAListar != None:
            Contratos = EquipoAListar.getContratos()
            for i in range(len(Contratos)):
                if Contratos[i] != None:
                    print(Contratos[i].getDiferenciaMeses())
                    print(Contratos[i].getImporteTotal())
                    Total += Contratos[i].getImporteTotal()
            print("Importe total de contratos del equipo {} es de: {}".format(nombre,Total))
        else:
            print("Equipo no encontrado")