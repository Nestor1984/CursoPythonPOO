"""
El Single Responsibility Principle (SRP), que en espanol se traduce como "Principio de Responsabilidad Unica",
es uno de los principios fundamentales en el desarrollo de software y la POO.
El SRP establece que cada clase o modulo en un programa debe tener una sola razon para cambiar, es decir, una
sola responsabilidad. Esto implica que una clase debe estar encapsulada con un Unico proposito o funcion dentro
del sistema. Cuando una clase o modulo tiene multiples responsabilidades, se vuelve mas dificil de entender, mantener
y modificar, lo cual puede conducir a codigo mas propenso a errores y menos flexible.
Aplicar el SRP suele implicar dividir clases o modulos grandes en clases mas pequenas y especializadas, cada una encargada
de una unica tarea bien definida. Esto no solo mejora la legibilidad y mantenibilidad del codigo, sino que tambien facilita
la reutilizacion de componentes y promueve practicas de diseno limpias y eficientes.
"""

class TanqueDeCombustible:
    def __init__(self):
        self.combustible = 100
    
    def agregar_combustible(self, cantidad):
        self.combustible += cantidad
        
    def obtener_combustible(self):
        return self.combustible
    
    def usar_combustible(self, cantidad):
        self.combustible -= cantidad

class Auto():
    def __init__(self, tanque): # Recibimos un objeto tanque de tipo TanqueDeCombustible
        self.posicion = 0 
        self.tanque = tanque
        
    def mover(self, distancia):
        if self.tanque.obtener_combustible() >= distancia / 2:
            self.posicion += distancia
            self.tanque.usar_combustible(distancia / 2)
            print("Has movido el auto exitosamente")
        else:
            print("No hay suficiente combustible")
            
    def obtener_posicion(self):
        return self.posicion
        
tanque = TanqueDeCombustible()
autito = Auto(tanque)

print(autito.obtener_posicion())
autito.mover(10)
print(autito.obtener_posicion())
autito.mover(20)
print(autito.obtener_posicion())
autito.mover(60)
print(autito.obtener_posicion())
autito.mover(100)
print(autito.obtener_posicion())
autito.mover(100)
print(autito.obtener_posicion())

"""
Salida:
0
Has movido el auto exitosamente
10
Has movido el auto exitosamente
30
Has movido el auto exitosamente
90
Has movido el auto exitosamente
190
No hay suficiente combustible
190
"""