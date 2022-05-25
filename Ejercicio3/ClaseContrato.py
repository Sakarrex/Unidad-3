from datetime import date, datetime

class Contrato:
    __fechaDeinicio = None
    __fechaDeFin = None
    __CostoMensual = -1
    __jugador = None
    __equipo = None

    def __init__(self, anioDeInicio,MesDeInicio,DiaDeInicio,anioDeFin,mesDeFin,diaDeFin,costoMensual, jugador = None, equipo = None):
        
        self.__fechaDeinicio = datetime(anioDeInicio,MesDeInicio,DiaDeInicio)
        self.__fechaDeFin = datetime(anioDeFin,mesDeFin,diaDeFin)
        self.__CostoMensual = costoMensual
        self.__jugador = jugador
        self.__equipo = equipo
    
    def __str__(self):
        return "Fecha de inicio: {}, Fecha de fin: {}, Costo Mensual: {}, jugador: ({}), Equipo: ({})".format(self.__fechaDeinicio,self.__fechaDeFin,self.__CostoMensual,self.__jugador,self.__equipo)
    
    def getFechaInicio(self):
        return self.__fechaDeinicio
    
    def getFechaFin(self):
        return self.__fechaDeFin
    
    def getCostoMensual(self):
        return self.__CostoMensual
    
    def getEquipo(self):
        return self.__equipo
    
    def getJugador(self):
        return self.__jugador
    
    
    def getDiferenciaMeses(self):
        return ((self.__fechaDeFin.year - self.__fechaDeinicio.year) * 12 + self.__fechaDeFin.month - self.__fechaDeinicio.month)
    
    def getImporteTotal(self):
        return self.getDiferenciaMeses() * self.__CostoMensual