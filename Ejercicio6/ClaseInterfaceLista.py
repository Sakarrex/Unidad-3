from zope.interface import Interface
from zope.interface import implementer

class ILista(Interface):

    def insertarElemento(self,elemento,pos):
        pass
    
    def AgregarElemento(self,elemento):
        pass

    def mostrarElemento(self,pos):
        pass

