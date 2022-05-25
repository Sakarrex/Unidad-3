class Jugador:
    __Nombre = str
    __DNI = str
    __CiudadNatal = str
    __PaisDeOrigen = str
    __FechaDeNacimiento = str
    __contrato = None

    def __init__(self, nombre = "vacio", DNI = "vacio", CiudadNatal = "vacio", paisDeorigen = "vacio", fechadenacimiento = "vacio", contrato = None):
        self.__Nombre = nombre
        self.__DNI = DNI
        self.__CiudadNatal = CiudadNatal
        self.__PaisDeOrigen = paisDeorigen
        self.__FechaDeNacimiento = fechadenacimiento 
        self.__contrato = contrato

    def agregarContrato(self,contrato):
        self.__contrato = contrato
    
    def __str__(self):
        return "Nombre: {}, DNI: {}, CiudadNatal: {}, PaisDeOrigen: {}, Fecha de nacimiento: {}".format(self.__Nombre,self.__DNI,self.__CiudadNatal,self.__PaisDeOrigen,self.__FechaDeNacimiento) 
    
    def getDNI(self):
        return self.__DNI

    def getContrato(self):
        return self.__contrato