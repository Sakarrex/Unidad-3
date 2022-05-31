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
            ListaDeAparatos.listarParaMi()
        elif switch == 4:
            Aparato = ListaDeAparatos.CrearAparato(input("Ingresar tipo de aparato: "))
            if Aparato != None:
                ListaDeAparatos.insertarElemento(Aparato,int(input("Ingeresar posicion: ")))
        elif switch == 5:
            ListaDeAparatos.mostrarElemento(int(input("Posicion: ")))
        elif switch == 6:
            ListaDeAparatos.ListarPhilips()
        elif switch == 7:
            ListaDeAparatos.ListarLavarropasSuperior()
        elif switch == 8:
            ListaDeAparatos.ListarTodosLosAparatos()
        elif switch == 9:
            UnObjectEncoder.guardarJSONArchivo(ListaDeAparatos.__toJSON__(),'aparatoselectronicos.json')
        elif switch == 10:
            ListaDeAparatos.getCabeza()
        else:
            print("Codigo erroneo")
        switch = int(input("switch: "))
        
'''
1
4
Televisor
Fravega
Modelo F
rojo
Portugal
90500
LCD
40
HD
False
3
3
















2
heladera
Philips
Modelo A
gris
Alemania
50000
60
True
False
2
televisor
Philips
Modelo B
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
Modelo C
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
Modelo D
Blanco
Inglaterra
750000
5
200
6
Superior
'''