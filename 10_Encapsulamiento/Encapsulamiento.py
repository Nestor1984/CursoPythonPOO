"""
El encapsulamiento: es el concepto de ocultar los detalles internos de una clase y exponer solo lo que es necesario.

Modificadores de ambito:
Publico (public)
Descripcion: Los atributos y metodos publicos son accesibles desde fuera de la clase.
Sintaxis: Sin prefijos especiales.
(atributo o metodo sin prefijo especial).

Protegido (protected)
Descripción: Los atributos y metodos protegidos estan destinados a ser accesibles solo
dentro de la clase y sus subclases. Esta es una convencion y no una restriccion estricta.
Sintaxis: Prefijo de un solo guion bajo (_).
(_atributo o _metodo).

Privado (private)
Descripcion: Los atributos y metodos privados estan destinados a ser accesibles solo dentro
de la clase donde se definen. Python usa un mecanismo de name mangling para ocultar estos miembros.
Sintaxis: Prefijo de dos guiones bajos (__).
(__atributo o __metodo).
"""

class MiClase:
    def __init__(self):
        self.__atributo_privado = "Valor" # Atributo privado (private)
    
    def __hablar(self): # Metodo privado (private)
        print("Hola, como estas")
        
        
objeto = MiClase()