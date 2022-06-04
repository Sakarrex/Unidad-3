
from ClaseNodo import Nodo
from zope.interface import interface
from zope.interface import implementer
from ClaseInterfaceLista import  ILista
from ClaseLavarropas import Lavarropas
from ClaseHeladera import Heladera
from ClaseTelevisor import Televisor
from ClaseInterfaceLista import ILista

@implementer(ILista)
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

        if self.__comienzo == None:
            self.__comienzo = NuevoNodo
            self.__actual = self.__comienzo
        else:
            aux = self.__comienzo
            while aux != None:
                aux = aux.getSiguiente()
            aux.setSiguiente(NuevoNodo)

        self.__tope += 1
    
    def getCabeza(self):
       print(self.__comienzo.getAparato())
        
        


    def insertarElemento(self,elemento,pos):
        if self.__tope < pos:
            raise IndexError
        
        NuevoNodo = Nodo(elemento)
        aux = self.__comienzo
        i = 1
        if pos == 1:
            NuevoNodo.setSiguiente(self.__comienzo)
            self.__comienzo = NuevoNodo
            self.__actual = self.__comienzo
        else:
            while aux.getSiguiente() != None and i < (pos-1):
                i += 1
                aux = aux.getSiguiente()
            if (pos-1) == i:
                    print("entra")
                    
                    NuevoNodo.setSiguiente(aux.getSiguiente())
                    aux.setSiguiente(NuevoNodo)
                    self.__tope += 1
       

    def listarParaMi(self):
        for i in self:
            print(i)
            print(i)
    
    def mostrarElemento(self,pos):
        if self.__tope < pos:
            raise IndexError

        aux = self.__comienzo
        band = False
        i=1
        print("pos:" + str(pos))
        while aux != None and band == False:
            print (i)
            if pos == i:
                print(aux.getAparato().__class__.__name__)
                band = True
            i+=1
            aux = aux.getSiguiente()
   
        
        
    
    def ListarPhilips(self):
        for i in self:
            if i.getMarca().lower() == "philips":
                print(i)

    def ListarLavarropasSuperior(self):
        for i in self:
            if isinstance(i,Lavarropas):
                if i.getCarga().lower() == "superior":
                    print(i.getMarca())
                
    def ListarTodosLosAparatos(self):
        for i in self:
            print(str(i.__class__.__name__) + " " + i.getMarca() +" "+ i.getPais() +" "+ str(i.ImporteDeVenta()))

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
