
from ClaseNodo import Nodo
from zope.interface import interface
from zope.interface import implementer
from ClaseAparato import Aparato
from ClaseLavarropas import Lavarropas
from ClaseHeladera import Heladera
from ClaseTelevisor import Televisor

class ListaDeProgramador:
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
        NuevoNodo = Nodo(elemento)
        NuevoNodo.setSiguiente(self.__comienzo)
        self.__comienzo = NuevoNodo
        self.__actual = NuevoNodo
        self.__tope += 1
    
   
        
        


    def insertarElemento(self,elemento,pos):
        try:
            aux = self.__comienzo
            ant = aux
            i = 0
            while aux.getSiguiente() != None and i<pos:
                if pos == i:
                    NuevoNodo = Nodo(elemento)
                    NuevoNodo.setSiguiente(aux.getSiguiente())
                    ant.setSiguiente(NuevoNodo)
                i+=1
                ant = aux
                aux = aux.getSiguiente()
        except IndexError:
            print("Posicion no encontrada")
    
    def mostrarElemento(self,pos):
        elementoADevolver = None
        try:
            aux = self.__comienzo
            band = False
            while aux.getSiguiente() != None and band == False:
                if pos == self.__indice:
                    self.__actual.getAparato()
   
        except IndexError:
            print("Posicion no encontrada")
        
        return elementoADevolver
    
    def CrearAparato(self,elemento):
        NuevoAparato = None
        if elemento.lower() == "heladera":
            NuevoAparato = Heladera(input("Marca: "),input("modelo: "), input("Color: "), input("pais: "), input("precio: "),input("capacidad de litros: "),bool(input("Freezer: ")),bool(input("ciclica: ")))
        elif elemento.lower() == "lavarropas":
            NuevoAparato = Lavarropas(input("Marca: "),input("modelo: "), input("Color: "), input("pais: "), input("precio: "),input("capacidad de lavado: "),input("velocidad de lavado: "),input("cantidad de programas: "),input("Tipo de carga: "))
        elif elemento.lower() == "televisor":
            NuevoAparato = Televisor(input("Marca: "),input("modelo: "), input("Color: "), input("pais: "), input("precio: "),input("tipo de pantalla: "),input("Pulgadas: "),input("Tipo de definicion: "),input("Conexion a internet: "))
        else:
            print("Aparato desconocido")
        return NuevoAparato
    
            
    def __toJSON__(self):
        d = dict(__class__ = self.__class__.__name__,
            Aparatos = [aparato.__toJSON__() for aparato in self])
        return d