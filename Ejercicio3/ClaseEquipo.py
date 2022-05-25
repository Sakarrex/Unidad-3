class Equipo:
    __nombre = str
    __ciudad = str
    __contratos = []

    def __init__(self, nombre = "vacio", ciudad = "vacio"):
        self.__nombre =  nombre
        self.__ciudad = ciudad
        self.__contratos = []
    
    def agregarContrato(self,contrato):
        self.__contratos.append(contrato)
    
    def getNombre(self):
        return self.__nombre
    
    def __str__(self):
        return "Nombre: {}, Ciudad: {}".format(self.__nombre,self.__ciudad)
    
    def getContratos(self):
        return self.__contratos