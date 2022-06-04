
from ClaseObjectEncoder import ObjectEncoder
from ClaseLista import ListaDeProgramador
from ClaseDocenteInvestigador import DocenteInvestigador
from ClasePersonal import Personal

if __name__ == '__main__':
    ListaDePersonal = ListaDeProgramador()
    UnObjectEncoder = ObjectEncoder()
    switch = int(input("1: Cargar Archivo\n2: Agregar Agente\n3: Insertar Agente\n4: Mostrar posicion\n5:Mostrar docentes investigadores por carrera\n6: Mostrar agentes por area de investigacion\n7: Listar todos los agentes\n8: Listar Docentes Investigadores por categoria\n9: Guardar archivo"))
    while switch != 0:
        if switch == 1:
            d = UnObjectEncoder.leerJSONArchivo("personal.json")
            ListaDePersonal = UnObjectEncoder.decodificarDiccionario(d)
        elif switch == 2:
            P = ListaDePersonal.GenerarPersonal(input("Ingresar tipo de personal: "))
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
            ListaDePersonal.MostrarPorArea(input("Ingreasar area de investigacion: "))
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
        switch = int(input("1: Cargar Archivo\n2: Agregar Agente\n3: Insertar Agente\n4: Mostrar posicion\n5:Mostrar docentes investigadores por carrera\n6: Mostrar agentes por area de investigacion\n7: Listar todos los agentes\n8: Listar Docentes Investigadores por categoria\n9: Guardar archivo"))

'''


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
9415-wfa21-214-g31
Antonio
Bertz
30000
2
LCC
exclusivo
Algortimos
Area B
Investigacion B
II
70000
2
Docente Investigador
1249-gae2-g3k4
Juan
Manolo
45000
10
LSI
exclusivo
Algortimos
Area A
Investigacion B
I
20000
2
Docente
9124-ji1-214f-123hi
Maria
Peralta
85000
6
TUPW
simple
Estructura y funcionamiento de computadoras
2
Investigador
124-912g12-12tui
Laura
Carmen
50000
3
Area A
Investigacion C
2
Docente Investigador
9415-wfa21-214-g31
Gustavo
Berenstein
30000
2
LCC
exclusivo
Algortimos
Area B
Investigacion B
II
40000


3
personal de apoyo
PRUEBA INSERTAR
Angela
Martinez
36000
2
15


'''        