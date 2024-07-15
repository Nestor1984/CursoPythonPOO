"""
MRO: Hace referencia al orden en el que python busca metodos y atributos en las clases.
"""

class A:
    def hablar(self):
        print("Hola desde A")

class B(A):
    def hablar(self):
        print("Hola desde B")

class C(A):
    def hablar(self):
        print("Hola desde C")
        
class D(B, C):
    pass
        
d = D()
"""
Invoca al metodo hablar() de la clase D como no hay, invoca al metodo hablar() de la clase B, si no hubiera un metodo hablar() en la clase B invocaria al
metodo hablar() de la clase C  y si no hubiera un metodo hablar() en la clase C invocaria al metodo hablar() de la clase A
"""
d.hablar()
"""
Salida:
Hola desde B
"""
# Mostramos el orden de ejecucion de la clase C
print(D.mro())
# Salida: [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]