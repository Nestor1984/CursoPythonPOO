"""
El Principio de Sustitucion de Liskov (Liskov's Substitution Principle, LSP) establece que los objetos de una clase derivada
(subclase) deben poder ser sustituidos por objetos de su clase base (superclase) sin afectar la integridad del programa. En otras palabras,
cualquier objeto de una subclase debe comportarse de la misma manera que su clase base cuando se utiliza en el codigo, sin introducir
comportamientos inesperados o errores.

Explicacion del ejemplo:
Ave es la clase base que define el metodo volar como un metodo abstracto que debe ser implementado por las subclases.
Pato y Aguila son subclases de Ave que sobrescriben el metodo volar para proporcionar la implementacion especifica de
como vuelan estos tipos de aves.
Ahora, aplicando el Principio de Sustitucion de Liskov:
La funcion hacer_volar toma un parametro de tipo Ave, que es la clase base. Segun el LSP, cualquier subtipo de Ave
(en este caso, Pato y Aguila) puede ser utilizado en lugar de Ave sin cambiar el comportamiento esperado del programa.
Cuando llamamos hacer_volar(mi_pato), el metodo volar de Pato es invocado y muestra el mensaje especifico para un pato.
Cuando llamamos hacer_volar(mi_aguila), el metodo volar de Aguila es invocado y muestra el mensaje especifico para un aguila.
"""

class Ave:
    def volar(self):
        pass

class Pato(Ave):
    def volar(self):
        print("El pato vuela utilizando sus alas.")

class Aguila(Ave):
    def volar(self):
        print("El aguila vuela majestuosamente en el cielo.")

def hacer_volar(ave):
    ave.volar()

# Crear instancias de las aves
mi_pato = Pato()
mi_aguila = Aguila()

# Llamando a la funcion haciendo_volar con diferentes tipos de aves
hacer_volar(mi_pato)
hacer_volar(mi_aguila)

"""
Salida:
El pato vuela utilizando sus alas.
El aguila vuela majestuosamente en el cielo.
"""
