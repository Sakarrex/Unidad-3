
from statistics import mode
import abc
from abc import ABC

class Calefactor(ABC):
    __marca = str
    __modelo = str
    def __init__(self,marca,modelo):
        self.__modelo = modelo
        self.__marca = marca
    
    def __str__(self):
        return "Modelo: {}, Marca: {} ".format(self.__modelo,self.__marca)