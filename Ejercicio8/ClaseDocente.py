
from ClasePersonal import Personal
import json


class Docente(Personal):
    __carrera = str
    __cargo = str
    __catedra = str
    __extraCargo = 0

    def __init__(self, cuil:str, nombre:str, apellido:str, sueldobasico:int, antiguedad:int,carrera:str,cargo:str,catedra:str,**kwargs):
        super().__init__(cuil, nombre, apellido, sueldobasico, antiguedad,**kwargs)
        self.__carrera = carrera
        self.__cargo = cargo
        self.__catedra = catedra
        self.__extraCargo = 0
        self.CalcularCargoextra()
    
    def getCarrera(self):
        return self.__carrera
    
    def getCargo(self):
        return self.__cargo
    
    def getCatedra(self):
        return self.__catedra

    
    def CalcularCargoextra(self):
        if self.__cargo.lower() == "simple":
            self.__extraCargo = self.getSueldoBasico()*0.1
        elif self.__cargo.lower() == "semiexclusivo":
            self.__extraCargo = self.getSueldoBasico() * 0.2
        elif self.__cargo.lower() == "exclusivo":
            self.__extraCargo += self.getSueldoBasico() * 0.5
        
    
    def SetExtraCargo(self, extraCargo):
        self.__extraCargo = extraCargo
        


    def calcularSueldo(self):
        SueldoADevolver = super().calcularSueldo() + self.__extraCargo
        return SueldoADevolver
        
    
    def __toJSON__(self):
        d = dict(__class__ = self.__class__.__name__,
            __atributos__ = dict(
                cuil = self.getCuil(),
                nombre = self.getNombre(),
                apellido = self.getApellido(),
                sueldobasico = self.getSueldoBasico(),
                antiguedad = self.getAntiguedad(),
                carrera = self.getCarrera(),
                cargo = self.getCargo(),
                catedra = self.getCatedra()
            )
        )
        return d
    
    def __str__(self):
        return super().__str__() + "Carrera: {}, Cargo: {}, Catedra: {}, Extra cargo: {}".format(self.__carrera,self.__cargo,self.__catedra,self.__extraCargo)