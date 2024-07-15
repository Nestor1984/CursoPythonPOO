"""
herencia multiple: se refiere a la capacidad que tiene una clase de heredar atributos y metodos de mas
de una clase base. Esto significa que una clase puede derivar comportamientos y caracteristicas de varias clases diferentes.
"""

# Superclase 1
class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        
    def hablar(self):
        print("Hola, estoy hablando un poco")

# Superclase 2
class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad
    
    def mostrar_habilidad(self):
        return f"Mi habilidad es: {self.habilidad}"

# Subclase
class EmpleadoArtista(Persona, Artista): # Esta Subclase hereda atributos y metodos de las dos Superclases Persona y Artista
    def __init__(self, nombre, edad, nacionalidad, habilidad, empresa, salario):    
        Persona.__init__(self, nombre, edad, nacionalidad) # Hacemos referencia al constructor de la clase Persona
        Artista.__init__(self, habilidad) # Hacemos referencia al constructor de la clase Artista
        self.empresa = empresa
        self.salario = salario
            
    def presentarse(self):
        print(f'Hola, soy: {self.nombre}, {super().mostrar_habilidad()} y trabajo en {self.empresa}') # Accedemos al metodo mostrar_habilidad() de la Superclase Artista
    
nestor = EmpleadoArtista("Nestor", 20, "Boliviano", "Cantar", "Google", 100000)
nestor.presentarse()

print()

herencia = issubclass(EmpleadoArtista, Artista) # Verificamos si EmpleadoArtista es una Subclase de Artista
print(herencia)

print() 

instancia = isinstance(nestor, EmpleadoArtista) # Verificamos si nestor es una instancia de EmpleadoArtista
print(instancia)

"""
Salida:
Hola, soy: Nestor, Mi habilidad es: Cantar y trabajo en Google

True
    
True
"""