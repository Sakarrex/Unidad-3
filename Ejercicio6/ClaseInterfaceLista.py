from zope.interface import interface


class ILista(interface):

    def insertarElemento(self,elemento,pos):
        pass
    
    def AgregarElemento(self,elemento):
        pass

    def mostrarElemento(self,pos):
        pass

