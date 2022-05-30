from ClaseObjectEncoder import ObjectoEnconder
from ClaseLista import ListaDeProgramador


if __name__ == "__main__":
    UnObjectEncoder = ObjectoEnconder()
    ListaDeAparatos = ListaDeProgramador()
    
    switch = int(input("switch: "))
    while switch != 0:
        if switch == 1:
            d = UnObjectEncoder.leerJSONArchivo('aparatoselectronicos.json')
            ListaDeAparatos = UnObjectEncoder.decodificarDiccionario(d) 
        elif switch == 2:
            Aparato = ListaDeAparatos.CrearAparato(input("Ingresar tipo de aparato: "))
            if Aparato != None:
                ListaDeAparatos.AgregarElemento(Aparato)
        elif switch == 3:
            for Aparato in ListaDeAparatos:
                print(Aparato)
        elif switch == 4:
            Aparato = ListaDeAparatos.CrearAparato(input("Ingresar tipo de aparato: "))
            if Aparato != None:
                ListaDeAparatos.insertarElemento(Aparato,int(input("Ingeresar posicion: ")))
        elif switch == 7:
            UnObjectEncoder.guardarJSONArchivo(ListaDeAparatos.__toJSON__(),'aparatoselectronicos.json')
        elif switch == 8:
            Aparato = ListaDeAparatos.CrearAparato(input("Ingresar tipo de aparato: "))
            print(Aparato.__toJSON__())
        else:
            print("Codigo erroneo")
        switch = int(input("switch: "))
        
'''
2
heladera
Philips
Marca A
gris
Alemania
50000
60
True
False
2
televisor
Philips
Marca B
Negro
Espania
35000
Led
55
HD
False
2
televisor
Musimundo
Marca C
Blanco
Estados Unidos
40000
Led
25
FULL HD
True
2
Lavarropas
Musimundo
Marca D
Blanco
Inglaterra
750000
5
200
6
Frontal
'''