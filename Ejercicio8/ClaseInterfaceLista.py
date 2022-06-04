from zope.interface import Interface
from zope.interface import implementer
class ILista(Interface):

    def insertarElemento(elemento,pos):
        pass
    
    def AgregarElemento(elemento):
        pass

    def mostrarElemento(pos):
        pass