
from ClasePersonal import Personal

class PersonalDeApoyo(Personal):
    __categoria = str
    __extraCategoria = int

    def __init__(self, cuil, nombre, apellido, sueldobasico, antiguedad,categoria,**kwargs):
        super().__init__(cuil, nombre, apellido, sueldobasico, antiguedad,**kwargs)
        self.__categoria = int(categoria)
        self.__extraCategoria = 0
        self.calcularCaregoria
    
    def __toJSON__(self):
        d = dict(__class__ = self.__class__.__name__,
            __atributos__ = dict(
                cuil = self.getCuil(),
                nombre = self.getNombre(),
                apellido = self.getApellido(),
                sueldobasico = self.getSueldoBasico(),
                antiguedad = self.getAntiguedad(),
                categoria = self.getCategoria()
            )
        )
        return d
    
    def getCategoria(self):
        return self.__categoria
    
    def calcularCaregoria(self):
        if 1 <= self.__categoria and self.__categoria <= 10:
            self.__extraCategoria += self.getSueldoBasico() * 0.1
        elif 11 <= self.__categoria and self.__categoria <= 20:
            self.__extraCategoria += self.getSueldoBasico() * 0.2
        elif 21 <= self.__categoria and self.__categoria <= 22:
            self.__extraCategoria += self.getSueldoBasico() * 0.3

    def setExtraCategoria(self, nuevoextraCategoria):
        self.extraCategoria = nuevoextraCategoria

    def calcularSueldo(self):
        SueldoAdevolver = super().calcularSueldo()+self.__extraCategoria
        return SueldoAdevolver
    
    def __str__(self):
        return super().__str__() + "Categoria: {}, extraPorCategoria: {}".format(self.__categoria,self.__extraCategoria)