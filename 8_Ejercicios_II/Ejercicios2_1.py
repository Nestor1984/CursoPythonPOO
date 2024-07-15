"""
Ejercicio de herencia multiple y MRO:

Imagina que estas modelando animales en un zoologico. Crear tres clases "Animal", "Mamifero" y
"Ave". La clase "Animal" debe tener un metodo llamado "comer". La clase "Mamifero" debe tener
un metodo llamado "amamantar" y la clase "Ave" un metodo llamado "volar".

Ahora, crea una clase "Murcielago" que herede de "Mamifero" y "Ave", en ese orden, y por lo tanto
debe ser capaz de "amamantar" y "volar", ademas de "comer".

Finalmente, juega con el orden de herencia de la clase "Murcielago" y observa como cambia el
MRO y el comportamiento de los metodos al usar super(). 
"""

class Animal:
    def comer(self):
        print("El animal esta comiendo")

class Ave(Animal):
    def volar(self):
        print("El animal esta volando")
        
class Mamifero(Animal):
    def amamantar(self):
        print("El animal esta amamantando")
        
class Murcielago(Mamifero, Ave):
    pass

murcielago = Murcielago()

murcielago.comer()
murcielago.amamantar()
murcielago.volar()
    
"""
Salida:
El animal esta comiendo
El animal esta amamantando
El animal esta volando
"""

print(Murcielago.mro())
# Salida: [<class '__main__.Murcielago'>, <class '__main__.Mamifero'>, <class '__main__.Ave'>, <class '__main__.Animal'>, <class 'object'>]