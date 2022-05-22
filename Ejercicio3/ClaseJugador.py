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