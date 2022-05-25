from operator import le
from ClaseRamo import Ramo
from ClaseContador import contadoresFlor

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
            Contador.append(contadoresFlor(0,i))

        for i in range(len(self.__listaRamos)):
            flores = self.__listaRamos[i].getFlores()
            for j in range(len(flores)):
                Contador[flores[j].getNumero()-1].sumarContador()
        
        #for i in range(len(Contador)):
            #print(str(Contador[i].getContador()) + " " + str(Contador[i].getCodigo()+1))
        Contador.sort()
        
        for i in range(5):
            print(ManejadorFlor.getFlorPorCodigo(Contador[i].getCodigo()))
        

    def MostrarTotalRamos(self):
        for i in range(len(self.__listaRamos)):
            Flores = self.__listaRamos[i].getFlores()
            for j in range(len(Flores)):
                print(Flores[j])

    def ContarFloresPorTamanioDeRamo(self,ManejadorFlor,tamanio):
        Contador = []
        tamanio = tamanio.lower()
        for i in range(ManejadorFlor.getTotalFlores()):
            Contador.append(contadoresFlor(0,i))

        for i in range(len(self.__listaRamos)):
            if self.__listaRamos[i].getTamano() == tamanio:
                flores = self.__listaRamos[i].getFlores()
                for j in range(len(flores)):
                    Contador[flores[j].getNumero()-1].sumarContador()
        
        #for i in range(len(Contador)):
            #print(str(Contador[i].getContador()) + " " + str(Contador[i].getCodigo()+1))
        Contador.sort()
        
        for i in range(len(Contador)):
            print(ManejadorFlor.getFlorPorCodigo(Contador[i].getCodigo()))