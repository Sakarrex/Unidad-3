
from xml.dom.minidom import CharacterData
from ClaseDocente import Docente
from ClaseInvestigador import Investigador

class DocenteInvestigador(Docente,Investigador):
    __categoriaProgramaIncentivos = str
    __importeExtraDocencia = int
    __investigacion = int

    def __init__(self, cuil, nombre, apellido, sueldobasico, antiguedad, carrera, cargo, catedra,areaDeInvestigacion,tipoDeInvestigacion,categoriaProgramaIncentivos,importeExtraDocencia,investigacion):
        super().__init__(cuil, nombre, apellido, sueldobasico, antiguedad, carrera, cargo, catedra,areaDeInvestigacion,tipoDeInvestigacion)
        self.__categoriaProgramaIncentivos = categoriaProgramaIncentivos
        self.__importeExtraDocencia = int(importeExtraDocencia)
        self.__investigacion = int(investigacion)
    
    def __toJSON__(self):
        d = dict(__class__ = self.__class__.__name__,
            __atributos__ = dict(
                cuil = self.getCuil(),
                nombre = self.getNombre(),
                apellido = self.getApellido(),
                sueldobasico = self.getSueldoBasico(),
                antiguedad = self.getAntiguedad(),
                carrera = self.getCarrera(),
                cargo = self.getCargo(),
                catedra = self.getCatedra(),
                areaDeInvestigacion = self.getAreaDeInvestigacion(),
                tipoDeInvestigacion = self.getTipoDeInvestigacion(),
                categoriaProgramaIncentivos = self.__categoriaProgramaIncentivos,
                importeExtraDocencia = self.__importeExtraDocencia,
                investigacion = self.__investigacion
            )
        )
        return d
    
    def getImporteDociencia(self):
        return self.__importeExtraDocencia
    
    def getImporteInvestigacion(self):
        return self.__investigacion

    
    def calcularSueldo(self):
        return Docente.calcularSueldo() + self.__importeExtraDocencia + self.__investigacion
    
    def __str__(self):
        return Docente().__str__() + Investigador.__str__() + "Categoria de Programa de Incentivos: {}, Importe Extra de Docencia: {}, Importe de Investigacion: {}".format(self.__categoriaProgramaIncentivos,self.__importeExtraDocencia,self.__investigacion)