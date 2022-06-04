
from ClaseDocente import Docente
from ClaseInvestigador import Investigador
from ClasePesonalDeApoyo import PersonalDeApoyo
from ClaseDocenteInvestigador import DocenteInvestigador
from ClaseNodo import Nodo
from zope.interface import implementer
from ClaseInterfaceLista import ILista
from ClaseIntefaceTesorero import ITesorero
from ClaseInterfaceDirector import IDirector

@implementer(ITesorero)
@implementer(IDirector)
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
        if self.__indice == self.__tope:
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

        if self.__comienzo == None:
            self.__comienzo = NuevoNodo
            self.__actual = self.__comienzo
        else:
            aux = self.__comienzo
            while aux.getSiguiente() != None:
                aux = aux.getSiguiente()
            aux.setSiguiente(NuevoNodo)

        self.__tope += 1
    
    def Insertar(self,dato,pos):
        if self.__tope < pos:
            raise IndexError
        
        NuevoNodo = Nodo(dato)
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
                if i.getAreaDeInvestigacion() == area:
                    contadorDocenteInvestigador += 1
            elif isinstance(i,Investigador):
                if i.getAreaDeInvestigacion() == area:
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
                if i.getCategoriaProgramaIncentivos() == categoria:
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
        
        if personal.lower() == "docente" or personal.lower() == "investigador" or personal.lower() == "docente investigador" or personal.lower() == "personal de apoyo": 
            cuil = input("Ingersar cuil:") 
            nombre= input("Ingresar nombre: ")
            apellido = input("Ingersar apellido: ")
            sueldobasico = int(input("Ingresar sueldobasico: "))
            antiguedad = int(input("Ingersar antiguedad: "))

            if personal.lower() == "docente":
                personalADevolver = Docente(cuil,nombre,apellido,sueldobasico,antiguedad,carrera=input("Carrera: "),cargo=input("cargo: "),catedra=input("Catedra: "))
            elif personal.lower() == "investigador":
                personalADevolver = Investigador(cuil=cuil,nombre=nombre,apellido=apellido,sueldobasico=sueldobasico,antiguedad=antiguedad,areaDeInvestigacion=input("AreaDeInvestigacion: "),tipoDeInvestigacion=input("Tipo de investigacion: "))
            elif personal.lower() == "docente investigador":
                personalADevolver = DocenteInvestigador(cuil,nombre,apellido,sueldobasico,antiguedad,carrera=input("Carrera: "),cargo=input("cargo: "),catedra=input("Catedra: "),areaDeInvestigacion=input("AreaDeInvestigacion: "),tipoDeInvestigacion=input("Tipo de investigacion: "),categoriaProgramaIncentivos=input("Categoria De incentivo: "),importeExtraDocenciaEInvestigacion=int(input("Importe extra docencia e investigacion: ")))
            elif personal.lower() == "personal de apoyo":
                personalADevolver = PersonalDeApoyo(cuil,nombre,apellido,sueldobasico,antiguedad,categoria=input("Categoria: "))
        else: 
            print("Personal no econtrado")
        return personalADevolver
    
    def gastosSueldoPorEmpleado(self,Cuil):
        bandera = False
        aux = self.__comienzo
        while aux != None and bandera == False:
            if aux.getDato().getCuil() == Cuil:
                print(aux.getDato().calcularSueldo())
                bandera = True
            aux = aux.getSiguiente()
        if bandera == False:
            print("Cuil no encontrado")
        
       
    
    def modificarBasico(self,cuil,nuevoBasico):
        bandera = False
        aux = self.__comienzo
        while aux != None and bandera == False:
            if aux.getDato().getCuil() == cuil:
                aux.getDato().setSueldoBasico(nuevoBasico)
                bandera = True
            aux = aux.getSiguiente()
        if bandera == False:
            print("Cuil no encontrado")
    
    def modificarPorcentajeporcargo(self,cuil,nuevoPorcentajeCargo):
        bandera = False
        aux = self.__comienzo
        while aux != None and bandera == False:
            if aux.getDato().getCuil() == cuil:
                aux.getDato().SetExtraCargo(nuevoPorcentajeCargo)
                bandera = True
            aux = aux.getSiguiente()
        if bandera == False:
            print("Cuil no encontrado")
    
    def modificarPorcentajeporcategoría(self,cuil,nuevoPorcentajeCategoria):
        bandera = False
        aux = self.__comienzo
        while aux != None and bandera == False:
            if aux.getDato().getCuil() == cuil:
                aux.getDato().setExtraCategoria(nuevoPorcentajeCategoria)
                bandera = True
            aux = aux.getSiguiente()
        if bandera == False:
            print("Cuil no encontrado")
    
    def modificarImporteExtra(self,cuil,nuevoImporteExtra):
        bandera = False
        aux = self.__comienzo
        while aux != None and bandera == False:
            if aux.getDato().getCuil() == cuil:
                aux.getDato().setImporteDocienciaEInvestigacion(nuevoImporteExtra)
                bandera = True
            aux = aux.getSiguiente()
        if bandera == False:
            print("Cuil no encontrado")