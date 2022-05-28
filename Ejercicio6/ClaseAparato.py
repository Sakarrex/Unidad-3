class Aparato:
    __marca =  str
    __modelo = str
    __color = str
    __paisDeFabricacion = str
    __precioBase = int

    def __init__(self,marca,modelo,color,pais,precio):
        self.__marca = marca
        self.__modelo = modelo
        self.__color = color
        self.__paisDeFabricacion = pais
        self.__precioBase = int(precio)
    
    def ImporteDeVenta(self):
        pass