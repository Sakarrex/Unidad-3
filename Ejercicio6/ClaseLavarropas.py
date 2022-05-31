
from ClaseAparato import Aparato
import json
from pathlib import Path
class Lavarropas(Aparato):
    __capacidadLavado = int
    __VelocidadLavado = int
    __cantidadDeProgramas = int
    __tipoDeCarga = str

    def __init__(self, marca, modelo, color, pais, precio,capacidadLavado,velocidadLavado,cantidadDeProgramas,tipoDeCarga):
        super().__init__(marca, modelo, color, pais, precio)
        self.__capacidadLavado = int(capacidadLavado)
        self.__VelocidadLavado = int(velocidadLavado)
        self.__cantidadDeProgramas = int(cantidadDeProgramas)
        self.__tipoDeCarga = tipoDeCarga
    
    def __str__(self) -> str:
        return super().__str__() + "capacidad de lavado: {}Kg, Valocidad de lavado: {}rpm, Cantidad de programas: {}, Tipo de carga: {}".format(self.__capacidadLavado,self.__VelocidadLavado,self.__cantidadDeProgramas,self.__tipoDeCarga)

    def ImporteDeVenta(self):
        precioADevolver = self.getPrecio()
        if self.__capacidadLavado <= 5:
            precioADevolver += self.getPrecio()*0.01
        else:
            precioADevolver += self.getPrecio()*0.03
        return precioADevolver
    
    def getCarga(self):
        return self.__tipoDeCarga

    def __toJSON__(self):
        
        d = dict(__class__ = self.__class__.__name__,
            __atributos__ = dict(
                marca = self.getMarca(),
                modelo = self.getModelo(),
                color = self.getColor(),
                pais = self.getPais(),
                precio = self.getPrecio(),
                capacidadLavado = self.__capacidadLavado,
                velocidadLavado = self.__VelocidadLavado,
                cantidadDeProgramas = self.__cantidadDeProgramas,
                tipoDeCarga = self.__tipoDeCarga
            )
        )
        return d