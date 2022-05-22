from operator import le
from ClaseRamo import Ramo

class ManejadorDeRamos:
    __listaRamos = []

    def __init__(self):
        self.__listaRamos = []
    
    def CargarRamo(self, tamanio, ManejadorFlor):
        tamanio = tamanio.lower()
        NuevoRamo = Ramo(tamanio)

        if tamanio == "chico":
            for i in range(2):
                NuevoRamo.agregarFlor(ManejadorFlor.getFlorPorCodigo(int(input("Ingresar codigo de flor a añadir en ramo: "))-1))
        elif tamanio == "mediano":
            for i in range(4):
                NuevoRamo.agregarFlor(ManejadorFlor.getFlorPorCodigo(int(input("Ingresar codigo de flor a añadir en ramo: "))-1))
        elif tamanio == "grande":
            for i in range(6):
                NuevoRamo.agregarFlor(ManejadorFlor.getFlorPorCodigo(int(input("Ingresar codigo de flor a añadir en ramo: "))-1))
        else:
            print("tamaño incorrecto")
            NuevoRamo = None

        if NuevoRamo != None:
            self.__listaRamos.append(NuevoRamo)
    

    def ContarMayorCantidadFlores(self,ManejadorFlor):
        Contador = []
        for i in range(ManejadorFlor.getTotalFlores()):
            Contador.append([0,i])

        for i in range(len(self.__listaRamos)):
            flores = self.__listaRamos[i].getFlores()
            for j in range(len(flores)):
                Contador[flores[j].getNumero()-1][0] += 1
        
        for i in range(len(Contador)):
            print(str(Contador[i][0]) + str(Contador[i][1]+1))
        #Contador.sort(key = lambda y: y[0])
        
        #for i in range(5):
         #   print(ManejadorFlor.getFlorPorCodigo(Contador[i][1]))
        

    def MostrarTotalRamos(self):
        for i in range(len(self.__listaRamos)):
            Flores = self.__listaRamos[i].getFlores()
            for j in range(len(Flores)):
                print(Flores[j])