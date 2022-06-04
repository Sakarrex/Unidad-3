import os
from ClaseObjectEncoder import ObjectEncoder
from ClaseLista import ListaDeProgramador
from ClaseIntefaceTesorero import ITesorero
from ClaseInterfaceDirector import IDirector

if __name__ == '__main__':
    ListaDePersonal = ListaDeProgramador()
    UnObjectEncoder = ObjectEncoder()

    Usuario = input('Usuario: ')
    Contrasenia = input('Contrasenia: ')

    if Usuario == "uTesorero" and Contrasenia == "ag@74ck":
        print("Ingresando como tesorero")
        ListaDePersonal = ITesorero(ListaDePersonal)
        switch = int(input("1: Cargar Archivo\n2: Agregar Agente\n3: Insertar Agente\n4: Mostrar posicion\n5:Mostrar docentes investigadores por carrera\n6: Mostrar agentes por area de investigacion\n7: Listar todos los agentes\n8: Listar Docentes Investigadores por categoria\n9: Guardar archivo\n10: Buscar por Cuil sueldo\n"))
    
        while switch != 0:
            if os.name == "nt":
                os.system("cls")
            else:
                os.system("clear")
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
                ListaDePersonal.gastosSueldoPorEmpleado(input("Ingreasr cuil a buscar: "))
            elif switch == 11:
                for i in ListaDePersonal:
                    print(i)
            else:
                print("Codigo erroneo")
            switch = int(input("1: Cargar Archivo\n2: Agregar Agente\n3: Insertar Agente\n4: Mostrar posicion\n5:Mostrar docentes investigadores por carrera\n6: Mostrar agentes por area de investigacion\n7: Listar todos los agentes\n8: Listar Docentes Investigadores por categoria\n9: Guardar archivo\n10: Buscar por Cuil sueldo\n"))
    
    elif Usuario == "uDirector" and Contrasenia == "ufC77#!1":
        print("Ingresando como tesorero")
        ListaDePersonal = IDirector(ListaDePersonal)
        switch = int(input("1: Cargar Archivo\n2: Agregar Agente\n3: Insertar Agente\n4: Mostrar posicion\n5:Mostrar docentes investigadores por carrera\n6: Mostrar agentes por area de investigacion\n7: Listar todos los agentes\n8: Listar Docentes Investigadores por categoria\n9: Guardar archivo\n10: Modificar sueldo basico\n11: Modificar porcentaje por cargo\n12: Modificar porcentaje por categoria\n13: Modificar importe extra\n"))
        while switch != 0:
            if os.name == "nt":
                os.system("cls")
            else:
                os.system("clear")
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
                ListaDePersonal.modificarBasico(input("Ingresar cuil a buscar: "), int(input("Ingresar nuevo sueldo basico: ")))
            elif switch == 11:
                ListaDePersonal.modificarPorcentajeporcargo(input("Ingresar cuil a buscar: "), int(input("Ingersar nuevo extra por cargo: ")))
            elif switch == 12:
                ListaDePersonal.modificarPorcentajeporcategoría(input("Ingresar cuil a buscar: "), int(input("Ingresar nuevo nuevo extra por categoria: ")))
            elif switch == 13:
                ListaDePersonal.modificarImporteExtra(input("Ingresar cuil a buscar: "), int(input("Ingresar nuevo nuevo extra: ")))
            elif switch ==14:
                for i in ListaDePersonal:
                    print(i)
            else:
                print("Codigo erroneo")
            switch = int(input("1: Cargar Archivo\n2: Agregar Agente\n3: Insertar Agente\n4: Mostrar posicion\n5:Mostrar docentes investigadores por carrera\n6: Mostrar agentes por area de investigacion\n7: Listar todos los agentes\n8: Listar Docentes Investigadores por categoria\n9: Guardar archivo\n10: Modificar sueldo basico\n11: Modificar porcentaje por cargo\n12: Modificar porcentaje por categoria\n13: Modificar importe extra\n"))