from csv import reader
import csv
from ClaseFacultad import Facultad

class ManejadorFacultades:

    __ListaFacultades = []
    
    def __init__(self):
        self.__ListaFacultades = []

    def Carga(self):

        archivo = open("C:\\Users\\Usuario\\Desktop\\POO\\Unidad-3\\Ejercicio1\\facultades.csv")
        reader = csv.reader(archivo,delimiter = ",")



        bandera = True
        for file in reader:
            if bandera == True:
                bandera = False
                FacultadActual = file
                listaCarreras = []
            else:
                if file[0] == FacultadActual[0]:
                    listaCarreras.append(file)
                else:
                    self.__ListaFacultades.append(Facultad(FacultadActual[0],FacultadActual[1],FacultadActual[2],FacultadActual[3],FacultadActual[4],listaCarreras))
                    print("entra else")
                    FacultadActual = file
                    listaCarreras = []
        self.__ListaFacultades.append(Facultad(FacultadActual[0],FacultadActual[1],FacultadActual[2],FacultadActual[3],FacultadActual[4],listaCarreras))

        archivo.close        
                

    def MostrarFacultadesPunto1(self, valor):    
        print("Facultad: " + str(self.__ListaFacultades[valor-1].getNombre()))
        carrerasFacultad = self.__ListaFacultades[valor-1].getCarreras()
        for i in range(len(carrerasFacultad)):
            print("Nombre: {}\n Duracion: {}".format(carrerasFacultad[i].getNombre(),carrerasFacultad[i].getDuracion()))

    def MostrarCarreraPunto2(self,nombre):
        
        i=0
        bandera = False
        while i < len(self.__ListaFacultades) and bandera == False:
            CarrerasFacultadActual = self.__ListaFacultades[i].getCarreras()
            j = 0
            while j < len(CarrerasFacultadActual) and bandera == False:
                
                if CarrerasFacultadActual[j].getNombre() == nombre:
                    bandera = True
                    print("Codigo de carrera: "+ self.__ListaFacultades[i].getCodigo()+","+ CarrerasFacultadActual[j].getCodigo() +"\nNombre de facultad: "+ self.__ListaFacultades[i].getNombre() +"\nLocalidad de facultad: " + self.__ListaFacultades[i].getLocalidad())
                j+=1
            i += 1
        if bandera == False:
            print("carrera no encontrada")
