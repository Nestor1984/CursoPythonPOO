"""
Abstraccion: En su nivel mas basico, basicamente significa manejar la complejidad  ocultando todos los detalles innecesarios al
programador o al usuario y dandole solo las funcionalidades relevantes.
"""

class Auto():
    def __init__(self):
        self._estado = "apagado" # Atributo protegido
    
    def encender(self):
        self._estado = "encendido"
        print("El auto esta encendido")
        
    def conducir(self):
        if self._estado == "apagado":
            self.encender()
        print("Conduciendo el auto")
    
mi_auto = Auto()
"""
NOTA: Al invocar al metodo 'conducir()' ya hay abstraccion, por que el usuario no sabe que primero estoy viendo que el estado este
apagado y si el estado esta apagado lo encendemos, tampoco sabe como hace para encenderse y cuales son las funciones que realiza
y tampoco sabe como esta estructurado todo, yo solamente le oculto toda la logica interna y simplemente le doy un metodo que es conducir()
"""
mi_auto.conducir()
"""
Salida:
El auto esta encendido
Conduciendo el auto
"""