import json
from pathlib import Path
from ClaseLista import ListaDeProgramador
from ClaseHeladera import Heladera
from ClaseLavarropas import Lavarropas
from ClaseTelevisor import Televisor


class ObjectoEnconder:
    def decodificarDiccionario(self,d):
        if '__class__' not in d:
            return d
        else:
            class_name = d['__class__']
            class_ = eval(class_name)
            if class_name == "ListaDeProgramador":
                ListaAparatos = d['Aparatos']
                ClaseListaProgramador = class_()
                DAparato = ListaAparatos[0]
                for i in range(len(ListaAparatos)):
                    DAparato = ListaAparatos[i]
                    class_name = DAparato.pop('__class__')
                    class_ = eval(class_name)
                    atributos = DAparato['__atributos__']
                    UnAparato = class_(**atributos)
                    ClaseListaProgramador.AgregarElemento(UnAparato)
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
