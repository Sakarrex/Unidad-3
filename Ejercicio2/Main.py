import ManejadordeRamos

if __name__ == "__main__":
    switch = -1
    print("1: Registrar ramo vendido\n2: 5 flores mas vendidas\n3: Flores vendidas por tamaño de ramo\n0: Finalizar")
    switch = int(input())
    while switch != 0:
        if switch == 1:
            ManejadordeRamos.RegistrarRamoVendido(input("Ingresar tamaño: "))
        elif switch == 2:
            ManejadordeRamos.getFloresMasVendidas()
        elif switch == 3:
            ManejadordeRamos.floresMasVendidasPorTamañoDeRamo(input("Ingresar tamaño de ramo: "))
        else:
            print("Codigo erroneo")
        print("1: Registrar ramo vendido\n2: 5 flores mas vendidas\n3: Flores vendidas por tamaño de ramo\n0: Finalizar")
        switch = int(input())
    

#Ramo 1 chico = (Rosa roja, roja blanca)
#Ramo 2 mediano = (rosa roja, rosa roja, rosa blanca, margarita amarilla)
#ramo 3 mediano = (rosa roja, margarita amarilla, margarita amarilla, azucena violeta)