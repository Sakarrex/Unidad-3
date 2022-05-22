from ClaseJugador import Jugador

class ManejadorDeJugadores:
    __ListaJugadores = []

    def __init__(self):
        self.__ListaJugadores = []
    
    def CargarJugador(self):
        nombre = input("Ingresar nombre de jugador: ")
        DNI = input("Ingresar DNI de jugador: ")