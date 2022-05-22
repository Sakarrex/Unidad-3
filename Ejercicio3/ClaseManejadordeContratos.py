import imp
from ClaseContrato import Contrato
import numpy

class ManejadorDeContratos:
    __ArregloContratos = None

    def __init__(self):
        self.__ArregloContratos = numpy.empty(5, dtype=Contrato)