
from ClaseAparato import Aparato
import json
from pathlib import Path

class Nodo:
    __aparato = None
    __siguiente = None
    def __init__(self,aparato):
        self.__aparato = aparato
        self.__siguiente = None
    
    def setSiguiente(self,siguiente):
        self.__siguiente = siguiente
    
    def getSiguiente(self):
        return self.__siguiente
    
    def getAparato(self):
        return self.__aparato
    
    def toJSON(self):
        d = dict(__class__ = self.__class__.__name__,
                __atributos__ = dict(
                aparato = self.__aparato,
                siguiente = self.__siguiente
            )
        )

        return d