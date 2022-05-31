import abc
from abc import ABC
import json
from pathlib import Path

class Aparato(ABC):
    __marca =  str
    __modelo = str
    __color = str
    __paisDeFabricacion = str
    __precioBase = int

    def __init__(self,marca,modelo,color,pais,precio):
        self.__marca = marca
        self.__modelo = modelo
        self.__color = color
        self.__paisDeFabricacion = pais
        self.__precioBase = int(precio)
    
    def __str__(self) -> str:
        return "Marca: {}, Modelo: {}, Color: {}, Pais: {}, Precio: {}, " .format(self.__marca,self.__modelo,self.__color,self.__paisDeFabricacion,self.__precioBase)
    
    def getMarca(self):
        return self.__marca
    
    def getModelo(self):
        return self.__modelo
    
    def getColor(self):
        return self.__color
    
    def getPais(self):
        return self.__paisDeFabricacion
    
    def getPrecio(self):
        return self.__precioBase

    @abc.abstractclassmethod
    def ImporteDeVenta():
        pass

    