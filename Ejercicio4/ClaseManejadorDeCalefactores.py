
import csv
from ClaseCalefactor import Calefactor
import numpy
from ClaseCalefactorAGas import CalefactorAGas
from ClaseCalefactorElectrico import CalefactorElectrico

class ManejadorDeCalefactores:
    __ArregloCalefactores = None
    __minGas = 999999
    __minElectrico= 999999
    __MenorGas = None
    __MenorElectrico = None

    def __init__(self,dimension):
        self.__ArregloCalefactores = numpy.empty(dimension, dtype= Calefactor)
        self.__minGas = 99999
        self.__minElectrico = 999999
        self.__MenorGas = None
        self.__MenorElectrico = None
    
    def Cargar(self):
        i=0
        archivo1 = open("C:\\Users\\Usuario\\Desktop\\POO\\Unidad-3\\Ejercicio4\\calefactor-a-gas.csv")
        reader1 = csv.reader(archivo1,delimiter=",")
        for files in reader1:
            UnCalefactorGas = CalefactorAGas(files[0],files[1],files[2],files[3])
            self.__ArregloCalefactores[i] = UnCalefactorGas
            i+=1
        archivo1.close

        archivo2 = open("C:\\Users\\Usuario\\Desktop\\POO\\Unidad-3\\Ejercicio4\\calefactor-electrico.csv")
        reader2 = csv.reader(archivo2,delimiter=",")
        for files in reader2:
            UnCalefactorElectrico = CalefactorElectrico(files[0],files[1],files[2])
            self.__ArregloCalefactores[i] = UnCalefactorElectrico
            i+=1
        archivo2.close
    
    def CalcularCalefactorAGasMasOptimo(self,costo,cantidad):
        pos = -1
        for i in range(len(self.__ArregloCalefactores)):
            if isinstance(self.__ArregloCalefactores[i],CalefactorAGas):
                if (self.__ArregloCalefactores[i].getCalorias()/1000)*cantidad*costo < self.__minGas:
                    self.__minGas = (self.__ArregloCalefactores[i].getCalorias()/1000)*cantidad*costo
                    pos = i

        print("El calefactor a gas de menor costo es: {} con un costo de {}".format(self.__ArregloCalefactores[pos],self.__minGas))

        self.__MenorGas = self.__ArregloCalefactores[pos]

    
    def CalcularCalefactorElectricoMasOptimo(self,costo,cantidad):
        pos = -1
        for i in range(len(self.__ArregloCalefactores)):
            if isinstance(self.__ArregloCalefactores[i],CalefactorElectrico):
                if (self.__ArregloCalefactores[i].getPotencia()/1000)*cantidad*costo < self.__minElectrico:
                    self.__minElectrico = (self.__ArregloCalefactores[i].getPotencia()/1000)*cantidad*costo
                    pos = i

        print("El calefactor electrico de menor costo es: {} con un costo de {}".format(self.__ArregloCalefactores[pos],self.__minElectrico))

        self.__MenorElectrico = self.__ArregloCalefactores[pos]
    
    def CompararMenorCalefactor(self):
        if self.__MenorGas != None and self.__MenorElectrico != None:
            print("entra")
            if self.__minElectrico < self.__minGas:
                print("Calefactor de menor costo: \n Tipo: Electrico, {}".format(self.__MenorElectrico))   
            else:  
                print("Calefactor de menor costo: \n Tipo: A gas, {}".format(self.__MenorGas))   

        

