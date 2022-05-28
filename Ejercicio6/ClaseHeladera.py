from ClaseAparato import Aparato

class Heladera(Aparato):
    __capacidadLitros = str
    __Freezer = bool
    __ciclica = bool

    def __init__(self, marca, modelo, color, pais, precio,capacidadLitros,freezer,ciclica):
        super().__init__(marca, modelo, color, pais, precio)
        self.__capacidadLitros = capacidadLitros
        self.__ciclica = ciclica
        self.__Freezer = freezer
    
    def ImporteDeVenta(self):
        precioADevolver = super().__precioBase
        if self.__Freezer == True:
            precioADevolver +=  super().__precioBase*0.01
        else:
            precioADevolver += super().__precioBase*0.05
        if self.__ciclica == True:
            precioADevolver += super().__precioBase*0.1
        return precioADevolver