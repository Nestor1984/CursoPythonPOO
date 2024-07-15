"""
El polimorfismo: es uno de los pilares basicos en la programación orientada a objetos.
El termino polimorfismo tiene origen en las palabras poly (muchos) y morfo (formas), y
aplicado a la programacion hace referencia a que los objetos pueden tomar diferentes formas.
"""
# Polimorfismo de Herencia
class Animal():
     # Metodo sonido en la clase base. Este metodo no hace nada y es un "metodo abstracto" (Espera que las subclases lo implementen)
    def sonido(self):
        pass

class Gato(Animal):
    # Implementación del metodo sonido para la clase Gato
    def sonido(self):
        return "Miau"
    
class Perro(Animal):
    # Implementacion del metodo sonido para la clase Perro
    def sonido(self):
        return "Guau"
    
def hacer_sonido(animal):
    print(animal.sonido())
    
gato = Gato()
perro = Perro()

hacer_sonido(gato)
print(gato.sonido())

hacer_sonido(perro)
print(perro.sonido())

"""
Salida:
Miau
Miau
Guau
Guau
"""