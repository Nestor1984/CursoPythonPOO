"""
Metodos especiales: son funciones que tienen un nombre especial reservado, inician con (__) y terminan con (__)
"""

class Persona:
    def __init__(self, nombre, edad): # __init__(): Este es el constructor de la clase.
        self.nombre = nombre
        self.edad = edad
        
    def __str__(self): # __str__(): Este metodo devuelve una presentacion del objeto en una cadena de texto.
        return f'Persona(nombre={self.nombre},edad={self.edad})'
    
    def __repr__(self): # __repr__(): Este metodo devuelve una cadena que podria ser usada para recrear el objeto original.
        return f'Persona("{self.nombre}", {self.edad})'
    
    def __add__(self, otro): # __add__(): Este metodo define el comportamiento de la suma (+) entre dos objetos Persona.
        nuevo_valor = self.edad + otro.edad
        return Persona(self.nombre+otro.nombre, nuevo_valor)
    
dalto = Persona("Lucas", 21)
pedro = Persona("Lucas", 30)
maria = Persona("Maria", 18)

print(dalto) # Imprime el resultado de __str__, mostrando: Persona(nombre=Lucas,edad=21)
print()

repre = repr(dalto) 
print(repre) # Imprime el resultado de __repr__, mostrando: Persona("Lucas", 21)
print()

nueva_persona = dalto + maria # Suma los atributos de dalto y maria usando __add__
print(nueva_persona.nombre) # Imprime el nombre de la nueva persona creada
print(nueva_persona.edad)  # Imprime la edad de la nueva persona creada

"""
Salida:
Persona(nombre=Lucas,edad=21)

Persona("Lucas", 21)

LucasMaria
39
"""