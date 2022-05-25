from datetime import date, datetime

class Contrato:
    __fechaDeinicio = None
    __fechaDeFin = None
    __CostoMensual = -1
    __jugador = None
    __equipo = None

    def __init__(self, anioDeInicio,MesDeInicio,DiaDeInicio,anioDeFin,mesDeFin,diaDeFin,costoMensual, jugador = None, equipo = None):
        formatFecha = "%d/%m/%Y %H:%M:&S.%f"
        fechainicio = datetime(anioDeInicio,MesDeInicio,DiaDeInicio)
        self.__fechaDeinicio = datetime.strptime(str(fechainicio),formatFecha)
        fechaFin =  datetime(anioDeFin,mesDeFin,diaDeFin)
        self.__fechaDeFin = datetime.strptime(str(fechaFin),formatFecha)
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