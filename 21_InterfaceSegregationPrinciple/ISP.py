"""
El ISP "Principio de Segregacion de Interfaces" establece que un cliente no debe ser obligado a depender de interfaces
que no utiliza. En otras palabras, es preferible tener interfaces mas especificas que multiples interfaces generales. Este
principio promueve la idea de dividir interfaces grandes y poco cohesivas en interfaces mas pequenas y especificas, cada una
orientada a un conjunto especifico de responsabilidades.
"""
from abc import ABC, abstractmethod # Importamos la clase ABC para definir clases abstractas y el decorador abstractmethod para definir metodos abstractos

class Trabajador(ABC): # Clase Abstracta o Interfaz
    
    @abstractmethod
    def trabajar(self):
        pass
    
class Comedor(ABC): # Clase Abstracta o Interfaz
    
    @abstractmethod
    def comer(self):
        pass
    
class Durmiente(ABC): # Clase Abstracta o Interfaz
    
    @abstractmethod
    def dormir(self):
        pass
    
class Humano(Trabajador, Durmiente, Comedor):
    def comer(self): # Sobreescribimos del metodo comer() de la clase padre Comedor
        print("El humano esta comiendo")
    
    def trabajar(self): # Sobreescribimos del metodo trabajar() de la clase padre Trabajador
        print("El humano esta trabajando")
    
    def dormir(self): # Sobreescribimos del metodo dormir() de la clase padre Durmiente
        print("El humano esta durmiendo")
        
class Robot(Trabajador): 
    def trabajar(self): # Sobreescribimos del metodo trabajar() de la clase padre Trabajador
        print("El robot esta trabajando")
        
robot = Robot()
humano = Humano()

robot.trabajar()
humano.trabajar()
humano.comer()
humano.dormir()

"""
Salida:
El robot esta trabajando
El humano esta trabajando
El humano esta comiendo
El humano esta durmiendo
"""