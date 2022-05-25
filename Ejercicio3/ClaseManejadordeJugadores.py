from operator import contains
from ClaseJugador import Jugador

class ManejadorDeJugadores:
    __ListaJugadores = []

    def __init__(self):
        self.__ListaJugadores = []
    
    def CargarJugador(self, nombre, DNI, ciudadNatal, PaisDeOrigen, FechaDeNacimiento):
        jugador = Jugador(nombre,DNI,ciudadNatal,PaisDeOrigen,FechaDeNacimiento)
        self.__ListaJugadores.append(jugador)
        return jugador

    def getJugadorPorDNI(self,DNI):
        bandera = False
        i=0
        while i < len(self.__ListaJugadores) and bandera == False:
            if self.__ListaJugadores[i].getDNI() == DNI:
                contrato = self.__ListaJugadores[i].getContrato()
                print("Nombre de equipo del contrato: {}, Fecha fin Contrato: {}".format(contrato.getEquipo().getNombre(),contrato.getFechaFin()))
                bandera = True
            i+=1
        if bandera == False:
            print("jugador no encontrado")
    