"""
herencia: permite a la clase hija acceder a todos los metodos y tener las propiedades de la clase padre.

Sintaxis: 
NombreClaseHija(NombreClasePadre)

Notas:
super(): Esta funcion devuelve un objeto proxy que permite hacer referencia a la clase padre de la clase actual. Es
decir, super() te da acceso a los metodos y atributos de la clase padre desde la clase hija.
__init__: Este es el metodo especial en Python que se utiliza para inicializar objetos. Es el constructor de la clase.
(nombre, edad, nacionalidad): Son los parametros que se pasan al constructor de la clase padre. Estos valores son
tipicamente especificos de la instancia de la clase hija que se esta creando.
"""

# Clase Padre o Superclase
class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    
    def hablar(self):
        print("Hola, estoy hablando un poco")

# Clase Hija o Subclase
class Empleado(Persona): # Heredamos atributos y metodos de la clase padre Persona
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo = trabajo
        self.salario = salario
        
# Clase Hija o Subclase
class Estudiante(Persona): # Heredamos atributos y metodos de la clase padre Persona
    def __init__(self, nombre, edad, nacionalidad, notas, universidad):
        super().__init__(nombre, edad, nacionalidad)
        self.notas = notas
        self.universidad = universidad

nestor = Empleado("Nestor", 20, "Boliviano", "Programador", 100000)

print(nestor.nombre)
print(nestor.edad)
print(nestor.nacionalidad)
print(nestor.trabajo)
print(nestor.salario)
nestor.hablar()

"""
Salida:
Nestor
20
Boliviano
Programador
100000
Hola, estoy hablando un poco
"""