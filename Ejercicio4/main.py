
from ClaseManejadorDeCalefactores import ManejadorDeCalefactores

if __name__ == "__main__":
    UnManejadorDeCalefactores = ManejadorDeCalefactores(int(input("Cantidad calefactores: ")))
    UnManejadorDeCalefactores.Cargar()
    switch = (int(input("switch: ")))
    while switch !=0:
        if switch == 1:
            UnManejadorDeCalefactores.CalcularCalefactorAGasMasOptimo(int(input("Ingreasr costo por m3: ")),int(input("Ingresar Cantidad a consumir por m3: ")))
            
        elif switch == 2:
            UnManejadorDeCalefactores.CalcularCalefactorElectricoMasOptimo(int(input("Ingresar costo por m3: ")),int(input("Ingresar Cantidad a consumir por m3: ")))
        elif switch == 3:
            UnManejadorDeCalefactores.CompararMenorCalefactor()
        else:
            print("error")
        switch = (int(input("switch: ")))
    

'''
10
1
2
3
2
2
3

'''