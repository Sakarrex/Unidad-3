class Flor:
    __numero = int
    __nombre = str
    __color = str
    __descripcion = str

    def __init__(self, numero = -1, nombre = "Vacio", color = "Vacio", descripcion = "Vacio"):
        self.__numero = int(numero)
        self.__nombre = str(nombre)
        self.__color = str(color)
        self.__descripcion = str(descripcion)
    
    def __str__(self):
        return "Numero: {} Nombre: {} Color: {}".format(self.__numero,self.__nombre,self.__color)
    
    def getNumero(self):
        return self.__numero
    
    def getNombre(self):
        return self.__nombre
    
    def getColor(self):
        return self.__color