"""
El Dependency Inversion Principle "Principio de Inversion de Dependencias" establece dos cosas el primero es que los modulos de
alto nivel no tienen que depender de los de bajo nivel, sino que los dos tienen que depender de las abstracciones y lo segundo es que las
abstracciones a su vez no deben depender de los detalles, sino que los detalles depender de las abstracciones. 
"""
    
from abc import ABC, abstractmethod

class VerificadorOrtografico(ABC):
    @abstractmethod
    def verificar_palabra(self, palabra):
        pass
    
class Diccionario(VerificadorOrtografico):
    def verificar_palabra(self, palabra):
        # Logica para verificar palabras si esta en el diccionario
        pass
    
class CorrectorOrtografico:
    def __init__(self, verificador): # Recibimos un objeto de tipo Diccionario
        self.verificador = verificador
      
    def corregir_texto(self, texto):
        # Usamos el verificador para corregir texto
        pass

# Salida: Sin salida
      
    