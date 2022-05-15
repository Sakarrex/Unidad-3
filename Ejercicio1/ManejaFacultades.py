from csv import reader
import csv
from typing import List
from ClaseFacultad import Facultad

ListaFacultades = []

archivo = open("Facultades.csv")
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
            ListaFacultades.append(Facultad(FacultadActual[0],FacultadActual[1],FacultadActual[2],FacultadActual[3],FacultadActual[4],listaCarreras))
            FacultadActual = file
            listaCarreras = []

def MostrarFacultadesPunto1(valor):    
    print("Facultad: " + str(ListaFacultades[valor-1].getNombre()))
    carrerasFacultad = ListaFacultades[valor-1].getCarreras()
    for i in range(len(carrerasFacultad)):
        print("Nombre: {}\n Duracion: {}".format(carrerasFacultad[i].getNombre(),carrerasFacultad[i].getDuracion()))

def MostrarCarreraPunto2(nombre):
    
    i=0
    bandera = False
    while i < range(len(ListaFacultades)) and bandera == False:
        CarrerasFacultadActual = ListaFacultades[i].getNombre()
        j = 0
        while j < range(len(CarrerasFacultadActual)) and bandera == False:
            if CarrerasFacultadActual[j].getNombre() == nombre:
                bandera = True
                print("Codigo de carrera: "+ ListaFacultades[i].getCodigo()+","+ CarrerasFacultadActual[j].getCodigo() +"\nNombre de facultad: "+ ListaFacultades[i].getNombre() +"\nLocalidad de facultad: " + ListaFacultades[i].getLocalidad())
            j+=1
        i += 1
