from numpy import sort
from ClaseRamo import Ramo
import ManejadordeFlores

ListaRamos = []

def RegistrarRamoVendido(tamaño):
    nuevoRamo = Ramo(tamaño)
    floresRamo = nuevoRamo.getFlores()
    tamaño = tamaño.lower()
    if tamaño == "chico":
        for i in range(2):
            nuevoRamo.agregarFlor(ManejadordeFlores.getFlor(int(input("Ingresar codigo de flor a añadir en ramo: "))))
            
    elif tamaño == "mediano":
        for i in range(4):
            nuevoRamo.agregarFlor(ManejadordeFlores.getFlor(int(input("Ingresar codigo de flor a añadir en ramo: "))))
   
    elif tamaño == "grande":
        for i in range(6):
            floresRamo.append(ManejadordeFlores.getFlor(int(input("Ingresar codigo de flor a añadir en ramo: "))))
  
    else:
        print("Tamaño no valido")
    
    try:
        if floresRamo[0] != None:
            ListaRamos.append(nuevoRamo)
    except ValueError:
        print("Error al crear flores en ramo")

def getFloresMasVendidas():
    ContadorFlores = []
    for i in range(ManejadordeFlores.getCantidadDeFlores()):
        tupla = [0,i+1]
        ContadorFlores.append(tupla)
    for i in range(len(ListaRamos)):
        ListaFloresRamoactual = ListaRamos[i].getFlores()
        for j in range(len(ListaFloresRamoactual)):
            ContadorFlores[ListaFloresRamoactual[j].getnumero()-1][0] += 1

    ContadorFlores.sort(primerElem)
    print("Flores mas vendidas")  
    for i in range(5):
       print(ManejadordeFlores.getNombreFlor(ContadorFlores[i][1]-1))

def floresMasVendidasPorTamañoDeRamo(tamaño):
    ContadorFlores = []
    for i in range(ManejadordeFlores.getCantidadDeFlores()):
        tupla = [0,i+1]
        ContadorFlores.append(tupla)
    for i in range(len(ListaRamos)):
        if ListaRamos[i].getTamano() == tamaño:
            ListaFloresRamoactual = ListaRamos[i].getFlores()
            for j in range(len(ListaFloresRamoactual)):
                ContadorFlores[ListaFloresRamoactual[j].getnumero()-1][0] += 1
    ContadorFlores.sort(primerElem)
    print("Flores mas vendidas para ramo de tamaño: " + tamaño)
    for i in range(len(ContadorFlores)):
            print(ManejadordeFlores.getNombreFlor(ContadorFlores[i][1]-1))

def primerElem(tupla):
    return tupla[0]