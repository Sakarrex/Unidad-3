from abc import ABC
import abc



class Personal(ABC):
    __cuil: str
    __nombre = str
    __apellido = str
    __sueldoBasico = int
    __antiguedad = int

    def __init__(self,cuil:str,nombre:str,apellido:str,sueldobasico:int,antiguedad:int,**kwargs):
        self.__cuil = cuil
        self.__nombre = nombre
        self.__apellido = apellido
        self.__sueldoBasico = int(sueldobasico)
        self.__antiguedad = int(antiguedad)
    
    def getCuil(self):
        return self.__cuil
    
    def getNombre(self):
        return self.__nombre
    
    def getApellido(self):
        return self.__apellido
    
    def getSueldoBasico(self):
        return self.__sueldoBasico
    
    def getAntiguedad(self):
        return self.__antiguedad
    
    def __gt__(self,otro):
        if type(otro) == type(self):
            return self.__nombre < otro.getApellido()
    
    def calcularSueldo(self):
        return self.__sueldoBasico + self.__sueldoBasico * (self.__antiguedad /100)
    
    def __str__(self):
        return "Cuil: {}, Nombre: {}, Apellido: {}, Sueldo Basico: {}, Antiguedad: {}, ".format(self.__cuil, self.__nombre,self.__apellido,self.__sueldoBasico,self.__antiguedad)
    
        