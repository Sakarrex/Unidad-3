from ClaseManejadordeContratos import ManejadorDeContratos
from ClaseManejadordeJugadores import ManejadorDeJugadores
from ClaseManjeadordeEquipos import ManejadorDeEquipos


if __name__ == "__main__":
    UnManejadorDeEquipos = ManejadorDeEquipos()
    UnManejadorDeJugadores = ManejadorDeJugadores()
    UnManejadorDeContratos = ManejadorDeContratos()
    UnManejadorDeEquipos.Carga()

    switch = int(input("switch"))
    while switch != 0:
        if switch == 1:
            EquipoContrato = UnManejadorDeEquipos.getEquipo(input("Nombre de equipo del contrato: "))
            if EquipoContrato != None:
                Jugador = UnManejadorDeJugadores.CargarJugador(input("Nombre: "), input("DNI: "), input("Ciudad natal: "), input("Pais de origen: "), input("Fecha de nacimiento: "))
                UnManejadorDeContratos.CrearContrato(int(input("Anio de inicio: ")),int(input("Mes de inicio: ")),int(input("Dia de inicio: ")),int(input("Anio de Fin: ")),int(input("Mes de inicio: ")),int(input("Dia de inicio: ")), int(input("Costo Mensual: ")),Jugador, EquipoContrato)
            else:
                print("Equipo no encontrado")
        elif switch == 2:
            UnManejadorDeJugadores.getJugadorPorDNI(input("Ingresar DNI de jugador a buscar: "))
        elif switch == 6:
            UnManejadorDeContratos.MostrarContratos()
        elif switch == 7:
            UnManejadorDeEquipos.getBoca()
        else:
            print("codigo no valido")
        switch = int(input("switch"))

#Maradona 33452342 Cordoba Argentina 03/04/1950
#Ronaldo 23485234 Rio de Janeiro Brasil 25/06/1990
#Messi 20355234 Buenos Aires Argentina 15/01/1995
'''
1
Boca
Maradona
33452342
Cordoba
Argentina
03/04/1950
2020
05
24
2022
07
12
50500
1
Ronaldo
23485234
Rio de Janeiro
Brasil
25/06/1990
2015
01
20
2015
08
20
60350
1
Messi
20355234
Buenos Aires
Argentina
15/01/1995
2019
05
15
2022
10
04
100500

'''