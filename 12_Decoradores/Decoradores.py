"""
Un decorador: es una funcion que toma otra funcion y la envuelve para agregarle funcionalidades
adicionales. Esencialmente, un decorador permite extender o alterar el comportamiento de una funcion
de manera mas flexible y legible.
"""

# Ejemplo 1:
def decorador(funcion): # Este metodo recibe como parametro una funcion
    def funcion_modificada():
        print("Antes de llamar a la funcion")
        funcion() # Ejecutamos la funcion que le pasamos como parametro
        print("Despues de llamar a la funcion")
    return funcion_modificada # Retornamos la funcion sin ejecutarla

def saludo():
    print("Hola Nestor como andas")
    
# Esto es como declarar una funcion de tipo flecha en JavaScript
saludo_modificado = decorador(saludo) # Le enviamos como argumento la funcion saludo
saludo_modificado() # Ejecutamos la funcion saludo_modificado

"""
Antes de llamar a la funcion
Hola Nestor como andas
Despues de llamar a la funcion
"""

print()

# Ejemplo 2:
def decorador2(funcion2): # Este metodo recibe como parametro una funcion
    def funcion_modificada2():
        print("Antes de llamar a la funcion")
        funcion2() # Ejecutamos la funcion que le pasamos como parametro
        print("Despues de llamar a la funcion")
    return funcion_modificada2 # Retornamos la funcion sin ejecutarla

@decorador2 # Este metodo 'decorador' va tomar como argumento la funcion de abajo
def saludo2():
    print("Hola Nestor como andas")
    
saludo2() # Esto nos devuelve la funcion saludo2() decorada

"""
Antes de llamar a la funcion
Hola Nestor como andas
Despues de llamar a la funcion
"""