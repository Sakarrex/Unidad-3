
from ClaseDocente import Docente
from ClaseInvestigador import Investigador

class DocenteInvestigador(Docente,Investigador):
    __categoriaProgramaIncentivos = str
    __importeExtraDocenciaEInvestigacion= int
    
    def __init__(self, cuil, nombre, apellido, sueldobasico, antiguedad, carrera, cargo, catedra,areaDeInvestigacion,tipoDeInvestigacion,categoriaProgramaIncentivos,importeExtraDocenciaEInvestigacion):
        #super().__init__(cuil, nombre, apellido, sueldobasico, antiguedad, carrera, cargo, catedra,areaDeInvestigacion,tipoDeInvestigacion)
        Docente.__init__(self,cuil, nombre, apellido, sueldobasico, antiguedad, carrera, cargo, catedra)
        Investigador.__init__(self,cuil, nombre, apellido, sueldobasico, antiguedad, areaDeInvestigacion, tipoDeInvestigacion)
        self.__categoriaProgramaIncentivos = categoriaProgramaIncentivos
        self.__importeExtraDocenciaEInvestigacion = int(importeExtraDocenciaEInvestigacion)

    
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
                importeExtraDocenciaEInvestigacion = self.__importeExtraDocenciaEInvestigacion   
            )
        )
        return d
    
    def getImporteDocienciaEInvestigacion(self):
        return self.__importeExtraDocenciaEInvestigacion


    
    def calcularSueldo(self):
        return Docente.calcularSueldo() + self.__importeExtraDocenciaEInvestigacion
    
    def __str__(self):
        return Docente().__str__() + Investigador.__str__() + "Categoria de Programa de Incentivos: {}, Importe Extra de Docencia: {}, Importe de Investigacion: {}".format(self.__categoriaProgramaIncentivos,self.__importeExtraDocencia,self.__investigacion)