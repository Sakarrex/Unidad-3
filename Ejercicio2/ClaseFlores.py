class Flores:
    __numero = int
    __nombre = str
    __color = str
    __descripcion = str

    def __init__(self, numero = -1, nombre = "Vacio", color = "Vacio", descripcion = "Vacio"):
        self.__numero = numero
        self.__nombre = nombre
        self.__color = color
        self.__descripcion = descripcion
    
    def getnumero(self):
        return self.__numero
    
    def getNombre(self):
        return self.__nombre