"""
Los setters y getters: son metodos que se utilizan para acceder y modificar los atributos de una clase de manera controlada.

Getter:
Descripcion: Un getter es un metodo que se utiliza para obtener el valor de un atributo privado de una clase. Proporciona acceso
a los valores de los atributos de forma controlada.
Sintaxis: Generalmente se define con un nombre que comienza con get_ seguido del nombre del atributo.

Setter:
Descripcion: Un setter es un metodo que se utiliza para establecer o modificar el valor de un atributo privado de una clase.
Sintaxis: Generalmente se define con un nombre que comienza con set_ seguido del nombre del atributo.
"""

class Persona:
    def __init__(self, nombre, edad):
        # Atributos privados (private)
        self.__nombre = nombre
        self.__edad = edad
        
    # Obtener nombre
    def get_nombre(self):
        return self.__nombre
    
    # Establecer nombre
    def set_nombre(self, new_nombre):
        self.__nombre = new_nombre
    
# Instanciamos la clase Persona
nestor = Persona("Jhoel", 20)

nombre = nestor.get_nombre()
print(nombre)

nestor.set_nombre("Pepito")
nombre = nestor.get_nombre()
print(nombre)

"""
Salida:
Jhoel
Pepito
"""