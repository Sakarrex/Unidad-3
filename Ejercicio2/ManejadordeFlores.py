from csv import reader
import csv
import numpy
from ClaseFlores import Flores

archivo = open("c:\\Users\\Usuario\\Desktop\\POO\\Unidad-3\\Ejercicio2\\flores.csv")
try:
    reader = csv.reader(archivo, delimiter = ",")
    ArregloFlores = numpy.empty(len(list(reader)), dtype = Flores)

    i = 0
    for files in reader:
        nuevaFlor = Flores(files[0],files[1],files[2],files[3])
        ArregloFlores[i] = nuevaFlor
        i +=1

    archivo.close
except ValueError:
    print("Error al abrir el archivo")

def getFlor(codigo):
    return ArregloFlores[codigo-1]

def getCantidadDeFlores():
    return len(ArregloFlores)

def getNombreFlor(codigo):
    return ArregloFlores[codigo-1].getNombre()