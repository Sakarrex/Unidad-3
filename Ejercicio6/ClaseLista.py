from textwrap import indent
from ClaseNodo import Nodo
from zope.interface import interface
from zope.interface import implementer
from ClaseAparato import Aparato
from ClaseInterfaceLista import ILista


@implementer(ILista)
class Lista:
    __comienzo = None
    __actual = None
    __indice = 0
    __tope = 0

    def __init__(self) -> None:
        self.__comienzo = None
        self.__actual = None
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__indice == self.__tope:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            self.__indice += 1
            Aparato = self.__actual.getAparato()
            self.__actual = self.__actual.getSiguiente()
            return Aparato

    
    def AgregarElemento(self,elemento):
        Nodo = self.__comienzo
        while Nodo.getSiguiente() != None:
            Nodo = Nodo.getSiguiente()
        self.__tope += 1
        Nodo.setSiguiente(elemento)
    
    def insertarElemento(self,elemento,pos):
        try:
            while self.__actual.getSiguiente() != None and self.__indice < pos:
                if pos == self.__indice:
                    NuevoNodo = Nodo(elemento)
                    NuevoNodo.setSiguiente(self.__actual.getSiguiente())
                    self.__actual.setSiguiente(NuevoNodo)
        except IndexError:
            print("Posicion no encontrada")
    
    def mostrarElemento(self,pos):
        elementoADevolver = None
        try:
            while self.__actual.getSiguiente() != None and self.__indice < pos:
                if pos == self.__indice:
                    self.__actual.getAparato()
   
        except IndexError:
            print("Posicion no encontrada")
        
        return elementoADevolver
    
    def toJSON(self):
        d = dict(
            __class__ = self.__class__.__name__,
            __atributos__ = dict(
                comienzo = self.__comienzo,
                actual = self.__actual,
                indice = self.__indice,
                tope = self.__tope
            )
        ) 
        return d