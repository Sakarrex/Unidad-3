
from ClaseAparato import Aparato

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

    def ImporteDeVenta(self):
        precioADevolver = super().__precioBase
        if self.__tipoDeDefinicion == "SD":
            precioADevolver += super().__precioBase * 0.01
        elif self.__tipoDeDefinicion == "HD":
            precioADevolver += super().__precioBase * 0.02
        elif self.__tipoDeDefinicion == "FULL HD":
            precioADevolver += super().__precioBase * 0.03
        if self.__conexionAInternet == True:
            precioADevolver += super().__precioBase * 0.1
        return precioADevolver