
from ClaseObjectEncoder import ObjectEncoder
from ClaseLista import ListaDeProgramador
from ClaseDocenteInvestigador import DocenteInvestigador
from ClasePersonal import Personal

if __name__ == '__main__':
    ListaDePersonal = ListaDeProgramador()
    UnObjectEncoder = ObjectEncoder()
    switch = int(input("Switch: "))
    while switch != 0:
        if switch == 1:
            d = UnObjectEncoder.leerJSONArchivo("personal.json")
            ListaDePersonal = UnObjectEncoder.decodificarDiccionario(d)
        elif switch == 2:
            P = ListaDePersonal.GenerarPersonal(input("Ingresar tipo de personal: "))
            print(P)
            if P != None:
                ListaDePersonal.AgregarDato(P)
        elif switch == 3:
            P = ListaDePersonal.GenerarPersonal(input("Ingresar tipo de personal: "))
            if P != None:
                try:
                    ListaDePersonal.Insertar(P, int(input("Ingresar posicion: ")))
                except IndexError:
                    print("Posicion no valida")
        elif switch == 4:
            try:
                ListaDePersonal.MostrarElemento(int(input("Ingresar posicion: ")))
            except IndexError:
                print("Posicion no valida")
        elif switch == 5:
            ListaDePersonal.MostrarDocentesInvestigadores(input("Ingresar carrera: "))
        elif switch == 6:
            ListaDePersonal.MostrarPorArea(input("Ingreasr area de investigacion: "))
        elif switch == 7:
            ListaDePersonal.MostrarTodosAgentes()
        elif switch == 8:
            ListaDePersonal.DIPorCategoria(input("Ingresar categoria: "))
        elif switch == 9:
            UnObjectEncoder.guardarJSONArchivo(ListaDePersonal.__toJSON__(),"personal.json")
        elif switch == 10:
            for i in ListaDePersonal:
                print(i)

        else:
            print("Codigo erroneo")
        switch = int(input("Switch: "))

'''
cuil, apellido, nombre, sueldo básico y antigüedad 
clases, cargo, cátedra, área de investigación y tipo de investigación, categoría en el programa de incentivos de investigación, importe extra por docencia e investigación.

2
personal de apoyo
9032-325j2-325k
Maria
Laura
83245
5
15


2
Docente Investigador
["cuil"="81-1ga24-1ag21a","nombre"="Juan","apellido"="Carlos","sueldoBasico"=43000,"antiguedad"=4,"carrera"="LCC","cargo"="semiexclusivo","catedra"="Algoritmos","areaDeInvestigacion"="Area A","tipoDeInvestigacion"="Investigacion A","categoriaProgramaIncentivos"="I","importeExtraDocenciaEInvestigacion"=5000]


2
Docente Investigador
9415-wfa21-214-g31
Manuel
Perez
30000
2
LCC
exclusivo
Algortimos
Area A
Investigacion B
I
70000
2
Docente Investigador
1249-gae2-g3k4
Marcos
Manolo
45000
10
LSI
exclusivo
Algortimos
Area A
Investigacion B
I
70000

'''        