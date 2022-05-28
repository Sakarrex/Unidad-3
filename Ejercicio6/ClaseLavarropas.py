from ClaseAparato import Aparato

class Lavarropas(Aparato):
    __capacidadLavado = int
    __VelocidadLavado = int
    __cantidadDeProgramas = int
    __tipoDeCarga = str

    def __init__(self, marca, modelo, color, pais, precio,capacidadLavado,velocidadLavado,cantidadDeProgramas,tipoDeCarga):
        super().__init__(marca, modelo, color, pais, precio)
        self.__capacidadLavado = capacidadLavado
        self.__velocidadLavado = velocidadLavado
        self.__cantidadDeProgramas = cantidadDeProgramas
        self.__tipoDeCarga = tipoDeCarga
    
    def ImporteDeVenta(self):
        precioADevolver = super().__precioBase
        if self.__capacidadLavado <= 5:
            precioADevolver += super().__precioBase*0.01
        else:
            precioADevolver += super().__precioBase*0.03
        return precioADevolver