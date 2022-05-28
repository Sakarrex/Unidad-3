from zope.interface import interface
from zope.interface import implementer

class ILista(interface):

    def insertarElemento(elemento,pos):
        pass
    
    def AgregarElemento(elemento):
        pass

    def mostrarElemento(pos):
        pass