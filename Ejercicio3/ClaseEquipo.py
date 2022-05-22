class Equipo:
    __nombre = str
    __ciudad = str
    __contratos = []

    def __init__(self, nombre = "vacio", ciudad = "vacio"):
        self.__nombre =  nombre
        self.__ciudad = ciudad
        self.__contratos = []