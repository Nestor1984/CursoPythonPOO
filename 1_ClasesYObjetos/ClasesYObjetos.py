"""
Clase: Una clase es una plantilla o un modelo que define las propiedades y comportamientos comunes que tendran los objetos de ese tipo.
Objeto: Un objeto es una instancia de una clase.
Snake Case: es un estilo de escritura de identificadores (nombres de variables, funciones, etc.) que consiste en escribir palabras en minusculas
y separarlas mediante guiones bajos (_). Por ejemplo: nombre_de_variable.
Pascal Case: es otro estilo de escritura de identificadores utilizado en Python y otros lenguajes de programacion. En Pascal case, las palabras
dentro del identificador comienzan con mayuscula y no se utilizan separadores. Por ejemplo: NombreDeVariable
"""

class Celular():
    # Atributos estaticos (Para todos los objetos van a ser iguales)
    marca = "Samsung"
    modelo = "S23"
    camara = "48MP"
    
# Instanciamos una clase o creamos un objeto
celular1 = Celular()

# Mostramos sus propiedades o atributos
print(celular1.marca)
print(celular1.modelo)
print(celular1.camara)

"""
Salida:
Samsung
S23
48MP
"""