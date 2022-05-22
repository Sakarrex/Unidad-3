from datetime import date, datetime


class Contrato:
    __fechaDeinicio = None
    __fechaDeFin = None
    __jugador = None
    __equipo = None

    def __init__(self, anioDeInicio,MesDeInicio,DiaDeInicio,anioDeFin,mesDeFin,diaDeFin, jugador = None, equipo = None):
        self.__fechaDeinicio = datetime.datetime(anioDeInicio,MesDeInicio,DiaDeInicio)
        self.__fechaDeFin = datetime.datetime(anioDeFin,mesDeFin,diaDeFin)
        self.__jugador = jugador
        self.__equipo = equipo