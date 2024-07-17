"""
Clase abstracta: es una clase que no puede ser instanciada directamente, sino que esta disenada especificamente
para ser heredada por otras clases. Estas clases abstractas sirven como plantillas para otras clases que las extienden,
definiendo metodos que deben ser implementados por las clases hijas.

abc: es un modulo que proporciona las herramientas necesarias para trabajar con clases abstractas y metodos abstractos.
ABC: Es una clase especial en Python que sirve como base para crear clases abstractas. Las clases abstractas
no se pueden instanciar directamente y se utilizan como plantillas para otras clases.
abstractclassmethod: Es un decorador especial que se usa para definir metodos de clase abstractos dentro de 
una clase abstracta. Un metodo abstracto es uno que se declara en la clase base pero se espera que cada subclase
lo implemente de manera unica.
"""

from abc import ABC, abstractclassmethod

class Persona(ABC): # Persona ahora es una clase abstracta por que hereda de ABC
    @abstractclassmethod # Este decorador te obliga a implementar o declarar (con pass) este metodo en las subclases
    def __init__(self, nombre, edad, sexo, actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad
    
    @abstractclassmethod # Este decorador te obliga a implementar o declarar (con pass) este metodo en las subclases
    def hacer_actividad(self):
        pass
    
    def presentarse(self):
        print(f"Hola, me llamo: {self.nombre} y tengo {self.edad} anios")
        
class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)
        
    def hacer_actividad(self):
        print(f"Estoy estudiando: {self.actividad}")
        
class Trabajador(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)
        
    def hacer_actividad(self):
        print(f"Actualmente estoy trabajando en el rubro de: {self.actividad}")
    
pedrito = Estudiante("Pedrito", 25, "No Binario", "Programacion")
nestor = Trabajador("Nestor", 20, "Masculino", "Programacion")

nestor.presentarse()
nestor.hacer_actividad()
pedrito.presentarse()
pedrito.hacer_actividad()

"""
Salida:
Hola, me llamo: Nestor y tengo 20 anios
Actualmente estoy trabajando en el rubro de: Programacion
Hola, me llamo: Pedrito y tengo 25 anios
Estoy estudiando: Programacion
"""