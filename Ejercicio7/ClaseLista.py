from ClaseDocente import Docente
from ClaseInvestigador import Investigador
from ClasePesonalDeApoyo import PersonalDeApoyo
from ClaseDocenteInvestigador import DocenteInvestigador
from ClaseNodo import Nodo
from zope.interface import implementer
from ClaseInterfaceLista import ILista

@implementer(ILista)
class ListaDeProgramador:
    __comienzo = None
    __actual = None
    __indice = 0
    __tope = 0

    def __init__(self):
        self.__comienzo = None
        self.__actual = None
        self.__indice = 0
        self.__tope = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__actual == self.__tope:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            self.__indice += 1
            dato = self.__actual.getDato()
            self.__actual = self.__actual.getSiguiente()
            return dato
    
    def AgregarDato(self,dato):
        NuevoNodo = Nodo(dato)
        NuevoNodo.setSiguiente(self.__comienzo)
        self.__comienzo = NuevoNodo
        #print(self.__comienzo.getDato())
        self.__actual = NuevoNodo
        self.__tope += 1
    
    def Insertar(self,dato,pos):
        if self.__tope < pos:
            raise IndexError
        
        aux = self.__comienzo
        i = 1
        if pos == 0:
            self.AgregarElemento(dato)
        else:
            while aux != None and i < pos:
                i += 1
                aux = aux.getSiguiente()
            if pos == i:
                    print("entra")
                    NuevoNodo = Nodo(dato)
                    NuevoNodo.setSiguiente(aux.getSiguiente())
                    aux.setSiguiente(NuevoNodo)
                    self.__tope += 1

    def MostrarElemento(self,pos):
        if self.__tope < pos:
            raise IndexError    
        aux = self.__comienzo
        band = False
        i=1
        while aux != None and band == False:
           
            if pos == i:
                print(aux.getDato().__class__.__name__)
                band = True
            i+=1
            aux = aux.getSiguiente()
   
   
   
    
    #punto 4
    def MostrarDocentesInvestigadores(self,carrera):
        ListaDocentesInvestigadores = []
        for i in self:
            if isinstance(i,DocenteInvestigador):
                if i.getCarrera() == carrera:
                    ListaDocentesInvestigadores.append(i)
        
        ListaDocentesInvestigadores.sort()

        for i in ListaDocentesInvestigadores:
            print(i)
    
    #Mostrar docentes investigadores e investigadores por area, punto 5
    def MostrarPorArea(self,area):
        contadorDocenteInvestigador = 0
        contadorInvestigadores = 0
        for i in self:
            if isinstance(i,DocenteInvestigador):
                if self.getAreaDeInvestigacion() == area:
                    contadorDocenteInvestigador += 1
            elif isinstance(i,Investigador):
                if self.getAreaDeInvestigacion() == area:
                    contadorInvestigadores += 1
        print("Hay: {} Docentes Investigadores y {} Investigadores en el area {}".format(contadorDocenteInvestigador, contadorInvestigadores,area))
    

    #punto 6
    def MostrarTodosAgentes(self):
        lista = []
        for i in self:
            lista.append(i)
        lista.sort()

        for i in lista:
            print("Nombre: {}, Apellido: {}, Tipo de Agente: {}, Sueldo: {}".format(i.getNombre(),i.getApellido(),i.__class__.__name__,i.calcularSueldo()))
    
    #Punto 7 preguntar
    def DIPorCategoria(self,categoria):
        Total = 0
        for i in self:
            if isinstance(i,DocenteInvestigador):
                if i.getAreaDeInvestigacion() == categoria:
                    print("Nombre: {}, Apellido: {}, Importe Extra: {}".format(i.getNombre(),i.getApellido(),i.getImporteDocienciaEInvestigacion()))
                    Total += i.getImporteDocienciaEInvestigacion()
        
        print("Total de importes extra: " + str(Total))

    
    def __toJSON__(self):
        d = dict(__class__ = self.__class__.__name__,
            ListaPersonal = [personal.__toJSON__() for personal in self]
        )
        return d
    

    def GenerarPersonal(self,personal):
        personalADevolver = None
        if personal.lower() == "docente":
            personalADevolver = Docente(input("Cuil:"),input("Nombre: "), input("Apellido: "),int(input("SueldoBasico:")),int(input("Antiguedad: ")),input("Carrera: "),input("cargo: "),input("Catedra: "))
        elif personal.lower() == "investigador":
            personalADevolver = Investigador(input("Cuil:"),input("Nombre: "), input("Apellido: "),int(input("SueldoBasico:")),int(input("Antiguedad: ")),input("AreaDeInvestigacion: "),input("Tipo de investigacion: "))
        elif personal.lower() == "docente investigador":
            personalADevolver = DocenteInvestigador(input("Cuil:"),input("Nombre: "), input("Apellido: "),int(input("SueldoBasico:")),int(input("Antiguedad: ")),input("Carrera: "),input("cargo: "),input("Catedra: "),input("AreaDeInvestigacion: "),input("Tipo de investigacion: "),input("Categoria De incentivo: "),int(input("Importe extra docencia e investigacion: ")))
        elif personal.lower() == "personal de apoyo":
            personalADevolver = PersonalDeApoyo(input("Cuil:"),input("Nombre: "), input("Apellido: "),int(input("SueldoBasico:")),int(input("Antiguedad: ")),input("Categoria: "))
        else: 
            print("Personal no econtrado")
        return personalADevolver