
from ClaseAparato import Aparato
import json
from pathlib import Path

class Televisor(Aparato):
    __tipoDePantalla = str
    __pulgadas = int
    __tipoDeDefinicion  = str
    __conexionAInternet = bool

    def __init__(self, marca, modelo, color, pais, precio,tipoPantalla,pulgadas,Definicion,conexionInternet):
        super().__init__(marca, modelo, color, pais, precio)
        self.__tipoDePantalla = tipoPantalla
        self.__pulgadas = int(pulgadas)
        self.__tipoDeDefinicion = Definicion
        self.__conexionAInternet = bool(conexionInternet)

    def __str__(self) -> str:
        return super().__str__() + "Tipo de pantalla: {}, pulgadas: {}, tipo de definicion: {}, conexion a internet: {}".format(self.__tipoDePantalla,self.__pulgadas,self.__tipoDeDefinicion,self.__conexionAInternet)


    def ImporteDeVenta(self):
        precioADevolver = self.getPrecio()
        if self.__tipoDeDefinicion == "SD":
            precioADevolver += self.getPrecio() * 0.01
        elif self.__tipoDeDefinicion == "HD":
            precioADevolver += self.getPrecio() * 0.02
        elif self.__tipoDeDefinicion == "FULL HD":
            precioADevolver += self.getPrecio() * 0.03
        if self.__conexionAInternet == True:
            precioADevolver += self.getPrecio() * 0.1
        return precioADevolver
    
    def __toJSON__(self):
        
        d = dict(__class__ = self.__class__.__name__,
            __atributos__ = dict(
                marca = self.getMarca(),
                modelo = self.getModelo(),
                color = self.getColor(),
                pais = self.getPais(),
                precio = self.getPrecio(),
                tipoPantalla = self.__tipoDePantalla,
                pulgadas = self.__pulgadas,
                Definicion = self.__tipoDeDefinicion,
                conexionInternet = self.__conexionAInternet
            )
        )
        return d