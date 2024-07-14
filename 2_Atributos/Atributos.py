"""
Atributos: Los atributos son variables que estan asociadas a objetos especificos creados a partir de una clase.
Metodo Constructor: es un tipo especial de metodo que se llama automaticamente cuando se crea una instancia (es decir, un objeto)
de una clase. Su proposito principal es inicializar los atributos del objeto.
self: es un convenio para referirse a la instancia actual de una clase. self permite que los metodos de una clase accedan a los
atributos y metodos de la misma instancia en la que estan siendo llamados
"""

class Celular:
    # Metodo Constructor
    def __init__(self, marca, modelo, camara): # Declaramos el parametro self y los otros 3 parametros que vamos a necesitar
        # Atributos
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
      
# Creamos un primer objeto    
celular1 = Celular("Samsung", "S23", "48MP") # Le enviamos los 3 argumentos que nos piden (nos olvidamos del self)
# Creamos un segundo objeto 
celular2 = Celular("Apple", "Iphone 15 Pro", "96MP") # Le enviamos los 3 argumentos que nos piden (nos olvidamos del self)

# Imprimimos
print(celular1.marca)
print(celular1.modelo)
print(celular1.camara)
print()
print(celular2.marca)
print(celular2.modelo)
print(celular2.camara)
"""
Salida:
Samsung
S23 
48MP

Apple
Iphone 15 Pro
96MP
"""