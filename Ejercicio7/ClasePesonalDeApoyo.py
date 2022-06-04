
from ClasePersonal import Personal

class PersonalDeApoyo(Personal):
    __categoria = str

    def __init__(self, cuil, nombre, apellido, sueldobasico, antiguedad,categoria):
        super().__init__(cuil, nombre, apellido, sueldobasico, antiguedad)
        self.__categoria = categoria
    
    def __toJSON__(self):
        d = dict(__class__ = self.__class__.__name__,
            __atributos__ = dict(
                cuil = self.getCuil(),
                nombre = self.getNombre(),
                apellido = self.getApellido(),
                sueldobasico = self.getSueldoBasico(),
                antiguedad = self.getAntiguedad(),
                categoria = self.__categoria
            )
        )
        return d
    
    def calcularSueldo(self):
        SueldoAdevolver = super().calcularSueldo()
        if 1 <= self.__categoria and self.__categoria <= 10:
            SueldoAdevolver = self.getSueldoBasico() * 0.1
        elif 11 <= self.__categoria and self.__categoria <= 20:
            SueldoAdevolver = self.getSueldoBasico() * 0.2
        elif 21 <= self.__categoria and self.__categoria <= 22:
            SueldoAdevolver = self.getSueldoBasico() * 0.3
        return SueldoAdevolver
    
    def __str__(self):
        return super().__str__() + "Categoria: {}".format(self.__categoria)