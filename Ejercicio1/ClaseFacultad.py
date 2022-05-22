from csv import reader
import csv

from ClaseCarrera import Carrera

class Facultad:

    __codigo = str
    __Nombre = str
    __direccion = str
    __localidad = str
    __Telefono = str
    __Carreras = []

    def __init__(self, codigo = "vacio", nombre = "vacio", direccion = "vacio", localidad = "vacio", telefono = "vacio", ListaCarreras = []):
        self.__codigo = str(codigo)
        self.__Nombre = str(nombre)
        self.__direccion = str(direccion)
        self.__localidad = str(localidad)
        self.__Telefono = str(telefono)
        self.__Carreras = []

        for i in range(len(ListaCarreras)):
            self.__Carreras.append(Carrera(ListaCarreras[i][1],ListaCarreras[i][2],ListaCarreras[i][3],ListaCarreras[i][4],ListaCarreras[i][5]))
    
    def getNombre(self):
        return self.__Nombre
    
    def getCarreras(self):
        return self.__Carreras
    
    def getCodigo(self):
        return self.__codigo
    
    def getLocalidad(self):
        return self.__localidad
    
    