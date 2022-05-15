import ManejaFacultades

if __name__ == "__main__":
    valor = -1
    print("1: mostrar nombre de la facultad, nombre  y duración de cada una de las carreras que se dictan en esa facultad.\n 2Dado el nombre de una carrera, mostrar código, nombre y localidad de la facultad donde esta se dicta.\n 0: finalizar")
    valor = int(input())
    while valor != 0:
        if valor == 1:
            ManejaFacultades.MostrarFacultadesPunto1(int(input("Ingresar codigo de facultad: ")))