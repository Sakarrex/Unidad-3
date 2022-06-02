from ClaseObjectEncoder import ObjectEncoder
from ClaseLista import ListaDeProgramador

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
            if P != None:
                ListaDePersonal.AgregarDato(P)
        elif switch == 3:
            ListaDePersonal.Insertar("a","B")
        elif switch == 4:
            ListaDePersonal.MostrarElemento(int(input("Ingresar posicion: ")))
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
        else:
            print("Codigo erroneo")
        switch = int(input("Switch: "))

'''
2
Docente Investigador
81-1ga24-1ag21a
Juan
Carlos
43000
4
LCC
semiexclusivo
Algortimos
Area A
Investigacion A
I
5000
9000
'''        