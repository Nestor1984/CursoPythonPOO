"""
Crear un juego de fusion.

El juego consiste en crear personajes un juego y que esos personajes se puedan fusionar
para formar personajes mas poderosos que tengan mas poder...

Para ello deberemos cambiar el comportamiento del operador "+" para que cuando los personajes
se fusionen, salga un nuevo personaje con habilidades mejoradas.

Una posible formula es: el promedio de las habilidades de ambos, al cuadrado!
"""

class Personaje:
    def __init__(self, nombre, fuerza, velocidad):
        self.nombre = nombre
        self.fuerza = fuerza
        self.velocidad = velocidad
        
    def __repr__(self):
        return f"{self.nombre} (Fuerza: {self.fuerza}, Velocidad: {self.velocidad})"
    
    def __add__(self, otro_pj):
        nuevo_nombre = self.nombre + "-" + otro_pj.nombre
        nueva_fuerza = ((self.fuerza + otro_pj.fuerza)/2)**2
        nueva_velocidad = ((self.velocidad + otro_pj.velocidad)/2)**2
        return Personaje(nuevo_nombre, nueva_fuerza, nueva_velocidad) # Retornamos un nuevo Personaje
    
goku = Personaje("Goku", 100, 100)
vegeta = Personaje("Vegeta", 99, 99)
print(goku)
print(vegeta)

gogeta = goku + vegeta # Hacemos uso del metodo '__add__'
print(gogeta)

"""
Salida:
Goku (Fuerza: 100, Velocidad: 100)
Vegeta (Fuerza: 99, Velocidad: 99)
Goku-Vegeta (Fuerza: 9900.25, Velocidad: 9900.25)
"""