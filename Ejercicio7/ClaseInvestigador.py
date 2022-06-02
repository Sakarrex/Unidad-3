from ClasePersonal import Personal

class Investigador(Personal):
    __areaDeInvestigacion = str
    __tipoDeInvestigacion = str

    def __init__(self, cuil, nombre, apellido, sueldobasico, antiguedad,areaDeInvestigacion,tipoDeInvestigacion):
        super().__init__(cuil, nombre, apellido, sueldobasico, antiguedad)
        self.__areaDeInvestigacion = areaDeInvestigacion
        self.__tipoDeInvestigacion = tipoDeInvestigacion

    def getAreaDeInvestigacion(self):
        return self.__areaDeInvestigacion
    
    def getTipoDeInvestigacion(self):
        return self.__tipoDeInvestigacion
    
    def __toJSON__(self):
        d = dict(__class__ = self.__class__.__name__,
            __atributos__ = dict(
                cuil = self.getCuil(),
                nombre = self.getNombre(),
                apellido = self.getApellido(),
                sueldobasico = self.getSueldoBasico(),
                antiguedad = self.getAntiguedad(),
                areaDeInvestigacion = self.__areaDeInvestigacion,
                tipoDeInvestigacion = self.__tipoDeInvestigacion
            )
        )
        return d
    
    
    def __str__(self):
        return super().__str__() + "Area de Investigacion: {}, Tipo de Investigacion: {}"