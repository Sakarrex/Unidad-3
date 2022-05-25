from ClaseMajadorDeFlores import ManejadorDeFlores
from ClaseManjadorDeRamos import ManejadorDeRamos

if __name__ == "__main__":
    ManejadorRamos = ManejadorDeRamos()
    ManejadorFlores = ManejadorDeFlores()
    ManejadorFlores.Carga()
    switch = -1
    print("1: Registrar ramo vendido\n2: 5 flores mas vendidas\n3: Flores vendidas por tamaño de ramo\n0: Finalizar")
    switch = int(input())
    while switch != 0:
        if switch == 1:
           ManejadorRamos.CargarRamo(input("Ingresar tamaño de ramo: "), ManejadorFlores)
        elif switch == 2:
           ManejadorRamos.ContarMayorCantidadFlores(ManejadorFlores)
        elif switch == 3:
           ManejadorRamos.ContarFloresPorTamanioDeRamo(ManejadorFlores, input("Ingresar tamanio de ramo: "))
        elif switch == 4:
            ManejadorRamos.MostrarTotalRamos()
        else:
            print("Codigo erroneo")
        print("1: Registrar ramo vendido\n2: 5 flores mas vendidas\n3: Flores vendidas por tamaño de ramo\n0: Finalizar")
        switch = int(input())
    

#Ramo 1 chico = (Rosa roja, roja roja)
#ramo 2 mediano = (rosa roja, rosa roja, rosa roja, rosa roja)
#Ramo 3 mediano = (rosa blanca, rosa blanca, rosa blanca, rosa blanca)
#ramo 4 mediano = (margarita amarilla, margarita amarilla, margarita amarilla ,azucena violeta)
#ramo 5 chico = (azucena cioleta, violeta violeta)

1
chico
3
3
1
mediano
3
3
3
3
1
mediano
6
6
6
6
1
mediano
9
9
9
7
1
chico
7
4
