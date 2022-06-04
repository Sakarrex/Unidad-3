
from ClaseDocente import Docente
from ClaseInvestigador import Investigador

class DocenteInvestigador(Docente,Investigador):
    __categoriaProgramaIncentivos = str
    __importeExtraDocenciaEInvestigacion= int
    
    def __init__(self, cuil:str, nombre:str, apellido:str, sueldobasico:int, antiguedad:int, carrera:str, cargo:str, catedra:str,areaDeInvestigacion:str,tipoDeInvestigacion:str,categoriaProgramaIncentivos:str,importeExtraDocenciaEInvestigacion:int,**kwargs) -> None:
        super().__init__(cuil=cuil, nombre=nombre, apellido=apellido, sueldobasico=sueldobasico, antiguedad=antiguedad, carrera=carrera, cargo=cargo, catedra=catedra, areaDeInvestigacion=areaDeInvestigacion, tipoDeInvestigacion=tipoDeInvestigacion, **kwargs)
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
                categoriaProgramaIncentivos = self.getCategoriaProgramaIncentivos(),
                importeExtraDocenciaEInvestigacion = self.getImporteDocienciaEInvestigacion()   
            )
        )
        return d
    
    def setImporteDocienciaEInvestigacion(self,NuevoImporte):
        self.__importeDocienciaEInvestigacion = NuevoImporte

    def getImporteDocienciaEInvestigacion(self):
        return self.__importeExtraDocenciaEInvestigacion

    def getCategoriaProgramaIncentivos(self):
        return self.__categoriaProgramaIncentivos
    
    def calcularSueldo(self):
        return Docente.calcularSueldo(self) + self.__importeExtraDocenciaEInvestigacion
    
    def __str__(self):
        return super().__str__() + "Categoria de Programa de Incentivos: {}, Importe Extra de Docencia E Investigacion: {}".format(self.__categoriaProgramaIncentivos,self.getImporteDocienciaEInvestigacion())