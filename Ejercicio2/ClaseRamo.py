
class Ramo:
    __tamaño = str
    __flores = []

    def __init__(self, tamaño = "vacio"):
        self.__tamaño = str(tamaño)
        self.__flores = []
    

    def agregarFlor(self, flor):
        self.__flores.append(flor)

    def getTamano(self):
        return self.__tamaño

    def getFlores(self):
        return self.__flores