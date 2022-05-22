from ClaseManejadorFacultades import ManejadorFacultades

if __name__ == "__main__":
    ManejadorFacu = ManejadorFacultades()
    ManejadorFacu.Carga()
    valor = -1
    print("1: mostrar nombre de la facultad, nombre  y duración de cada una de las carreras que se dictan en esa facultad.\n2: Dado el nombre de una carrera, mostrar código, nombre y localidad de la facultad donde esta se dicta.\n0: finalizar")
    valor = int(input())
    while valor != 0:
        if valor == 1:
            ManejadorFacu.MostrarFacultadesPunto1(int(input("Ingresar codigo de facultad: ")))
        if valor == 2:
            ManejadorFacu.MostrarCarreraPunto2(input("Ingrese nombre de carrera a buscar: "))
        print("1: mostrar nombre de la facultad, nombre  y duración de cada una de las carreras que se dictan en esa facultad.\n2: Dado el nombre de una carrera, mostrar código, nombre y localidad de la facultad donde esta se dicta.\n0: finalizar")
        valor = int(input())