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
                UnManejadorDeContratos.CrearContrato(int(input("Anio de inicio: ")),int(input("Mes de inicio: ")),int(input("Dia de inicio: ")),int(input("Anio de Fin: ")),int(input("Mes de fin: ")),int(input("Dia de fin: ")), int(input("Costo Mensual: ")),Jugador, EquipoContrato)
            else:
                print("Equipo no encontrado")
        elif switch == 2:
            UnManejadorDeJugadores.getJugadorPorDNI(input("Ingresar DNI de jugador a buscar: "))
        elif switch == 3:
            UnManejadorDeContratos.getContratosVencimiento6(input("Ingresar nombre de equipo: "))
        elif switch == 4:
            UnManejadorDeEquipos.getImporteTotal(input("Ingresar nombre de equipo: "))
        elif switch == 5:
            UnManejadorDeContratos.GuardarContratos()
        elif switch == 6:
            UnManejadorDeContratos.MostrarContratos()
        
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
500
1
River
Ronaldo
23485234
Rio de Janeiro
Brasil
25/06/1990
2015
01
20
2015
02
20
350
1
River
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
1500

'''