'''
import os
from ClaseObjectEncoder import ObjectEncoder
from ClaseLista import ListaDeProgramador
from ClaseIntefaceTesorero import ITesorero
from ClaseInterfaceDirector import IDirector

class Menu:
    __ListaDePersonal = None
    __UnObjectEncoder = None

    def __init__(self,listaPersonal) -> None:
        self.__ListaPersonal = listaPersonal
        self.__UnObjectEncoder = ObjectEncoder()

    def MostrarMenu(self):
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        if isinstance(self.__ListaDePersonal,ITesorero):
            print("1: Cargar Archivo\n2: Agregar Agente\n3: Insertar Agente\n4: Mostrar posicion\n5:Mostrar docentes investigadores por carrera\n6: Mostrar agentes por area de investigacion\n7: Listar todos los agentes\n8: Listar Docentes Investigadores por categoria\n9: Guardar archivo\n10: Buscar por Cuil sueldo\n")
        elif isinstance(self.__ListaPersonal,IDirector):
            input("1: Cargar Archivo\n2: Agregar Agente\n3: Insertar Agente\n4: Mostrar posicion\n5:Mostrar docentes investigadores por carrera\n6: Mostrar agentes por area de investigacion\n7: Listar todos los agentes\n8: Listar Docentes Investigadores por categoria\n9: Guardar archivo\n10: Modificar sueldo basico\n11: Modificar porcentaje por cargo\n12: Modificar porcentaje por categoria\n13: Modificar importe extra\n")
        self.SeleccionarOpcion()
    
    def SeleccionarOpcion(self):
        switch = int(input())
        if switch == 1:
                d = self._UnObjectEncoder.leerJSONArchivo("personal.json")
                __ListaDePersonal = self.__UnObjectEncoder.decodificarDiccionario(d)
        elif switch == 2:
                P = self.__ListaDePersonal.GenerarPersonal(input("Ingresar tipo de personal: "))
                if P != None:
                    self.__ListaDePersonal.AgregarDato(P)
        elif switch == 3:
                P = self.__ListaDePersonal.GenerarPersonal(input("Ingresar tipo de personal: "))
                if P != None:
                    try:
                        self.__ListaDePersonal.Insertar(P, int(input("Ingresar posicion: ")))
                    except IndexError:
                        print("Posicion no valida")
        elif switch == 4:
                try:
                    self.__ListaDePersonal.MostrarElemento(int(input("Ingresar posicion: ")))
                except IndexError:
                    print("Posicion no valida")
        elif switch == 5:
                self.__ListaDePersonal.MostrarDocentesInvestigadores(input("Ingresar carrera: "))
        elif switch == 6:
                self.__ListaDePersonal.MostrarPorArea(input("Ingreasar area de investigacion: "))
        elif switch == 7:
                self.__ListaDePersonal.MostrarTodosAgentes()
        elif switch == 8:
                self.__ListaDePersonal.DIPorCategoria(input("Ingresar categoria: "))
        elif switch == 9:
                self.__UnObjectEncoder.guardarJSONArchivo(self.ListaDePersonal.__toJSON__(),"personal.json")
        
        elif isinstance(self.ListaDePersonal,ITesorero):
            if switch == 10:
                self.__ListaDePersonal.gastosSueldoPorEmpleado(input("Ingreasr cuil a buscar: "))
    
        elif isinstance(self.ListaDePersonal,IDirector):
            if switch == 10:
                self.__ListaDePersonal.modificarBasico(input("Ingresar cuil a buscar: "), int(input("Ingresar nuevo sueldo basico: ")))
            elif switch == 11:
                self.__ListaDePersonal.modificarPorcentajeporcargo(input("Ingresar cuil a buscar: "), int(input("Ingersar nuevo extra por cargo: ")))
            elif switch == 12:
                self.__ListaDePersonal.modificarPorcentajeporcategoría(input("Ingresar cuil a buscar: "), int(input("Ingresar nuevo nuevo extra por categoria: ")))
            elif switch == 13:
                self.__ListaDePersonal.modificarImporteExtra(input("Ingresar cuil a buscar: "), int(input("Ingresar nuevo nuevo extra: ")))
        else: 
            print("Codigo erroneo")
        self.MostrarMenu()
'''