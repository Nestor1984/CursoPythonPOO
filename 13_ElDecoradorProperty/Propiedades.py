"""
El decorador @property: se utiliza para definir metodos de una clase que se comportan como atributos,
en lugar de metodos normales. Esto te permite acceder a los metodos de una clase como si fueran atributos,
lo que puede hacer que tu codigo sea mas limpio y facil de leer.

¿Que Hace el Decorador @property?
El decorador @property permite que un metodo actue como un atributo de solo lectura. Esto significa que
puedes definir un metodo que se comporta como un atributo, de modo que puedes acceder a su valor sin necesidad
de parentesis como si fuera un atributo de instancia. Ademas, @property permite definir metodos de "getter",
"setter" y "deleter" para gestionar el acceso y la modificacion de los atributos de una manera controlada.
"""

class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre # Atributo privado
        self._edad = edad # Atributo protegido
        
    # Propiedad nombre - Getter:
    @property #  Este decorador convierte el metodo nombre en una propiedad de solo lectura
    def nombre(self):
        return self.__nombre
    
    # Propiedad nombre - Setter:
    @nombre.setter # Este decorador define un metodo setter para la propiedad nombre, permitiendo modificar el valor del atributo __nombre.
    def nombre(self, new_nombre):
        self.__nombre = new_nombre
        
    # Propiedad nombre - Deleter:
    @nombre.deleter # Este decorador define un metodo deleter para la propiedad nombre, que permite eliminar el atributo __nombre.
    def nombre(self):
        del self.__nombre
    
nestor = Persona("Jhoel", 20)

nombre = nestor.nombre # Obtenemos el nombre (NO HAY NECESIDAD DE USAR PARENTESIS)
print(nombre)

nestor.nombre = "Pepe" # Establecemos el nombre (NO HAY NECESIDAD DE USAR PARENTESIS)
nombre = nestor.nombre # Obtenemos el nombre (NO HAY NECESIDAD DE USAR PARENTESIS)
print(nombre)

del nestor.nombre # Eliminamos el nombre. Despues de esta operacion, el atributo __nombre ya no existira en la instancia (NO HAY NECESIDAD DE USAR PARENTESIS)

print("Que haces")

"""
Salida:
Jhoel
Pepe     
Que haces
"""