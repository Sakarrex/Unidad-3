from gc import freeze
from ClaseAparato import Aparato
import json
from pathlib import Path
class Heladera(Aparato):
    __capacidadLitros = int
    __Freezer = bool
    __ciclica = bool

    def __init__(self, marca, modelo, color, pais, precio,capacidadLitros,freezer,ciclica):
        super().__init__(marca, modelo, color, pais, precio)
        self.__capacidadLitros = int(capacidadLitros)
        self.__ciclica = bool(ciclica)
        self.__Freezer = bool(freezer)

    def __str__(self) -> str:
        return super().__str__() + "Capacidad de Litros: {}, Freezer: {}, Ciclica: {}".format(self.__capacidadLitros,self.__Freezer,self.__ciclica)

    def ImporteDeVenta(self):
        precioADevolver = super().__precioBase
        if self.__Freezer == True:
            precioADevolver += super().__precioBase*0.01
        else:
            precioADevolver += super().__precioBase*0.05
        if self.__ciclica == True:
            precioADevolver += super().__precioBase*0.1
        return precioADevolver
    
    def __toJSON__(self):
        d = dict(__class__ = self.__class__.__name__,
            __atributos__ = dict(
                marca = self.getMarca(),
                modelo = self.getModelo(),
                color = self.getColor(),
                pais = self.getPais(),
                precio = self.getPrecio(),
                capacidadLitros = self.__capacidadLitros,
                freezer = self.__Freezer,
                ciclica = self.__ciclica
            )
        )
        return d
