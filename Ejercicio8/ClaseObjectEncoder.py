import json
from pathlib import Path
from ClaseLista import ListaDeProgramador
from ClasePersonal import Personal
from ClaseDocente import Docente
from ClaseInvestigador import Investigador
from ClaseDocenteInvestigador import DocenteInvestigador
from ClasePesonalDeApoyo import PersonalDeApoyo

class ObjectEncoder:
    def decodificarDiccionario(self,d):
        if '__class__' not in d:
            return d
        else:
            class_name = d['__class__']
            class_ = eval(class_name)
            if class_name == "ListaDeProgramador":
                ListaPersonal = d['ListaPersonal']
                ClaseListaProgramador = class_()
                DPersonal = ListaPersonal[0]
                for i in range(len(ListaPersonal)):
                    DPersonal = ListaPersonal[i]
                    class_name = DPersonal.pop('__class__')
                    class_ = eval(class_name)
                    atributos = DPersonal['__atributos__']
                    UnPersonal = class_(**atributos)
                    ClaseListaProgramador.AgregarDato(UnPersonal)
            return ClaseListaProgramador               

        

    def guardarJSONArchivo(self, diccionario, archivo):
        with Path(archivo).open("w", encoding="UTF-8") as destino:
            json.dump(diccionario, destino, indent=4)
            destino.close() 
    
    def leerJSONArchivo(self,archivo):
        with Path(archivo).open(encoding="UTF-8") as fuente:
            diccionario=json.load(fuente)
            fuente.close()
            return diccionario

    def convertirTextoADiccionario(self, texto):
        json.loads(texto)