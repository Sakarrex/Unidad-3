class Carrera:
    __codigo = str
    __nombre = str
    __duracion = str
    __titulo = str
    __tipo = str

    def __init__(self, codigo = "vacio", nombre = "vacio",duracion = "vacio", titulo = "vacio", tipo = "vacio"):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__duracion = duracion
        self.__titulo = titulo
        self.__tipo = tipo
    
    def getNombre(self):
        return self.__nombre

    def getDuracion(self):
        return self.__duracion
    
    def getCodigo(self):
        return self.__codigo