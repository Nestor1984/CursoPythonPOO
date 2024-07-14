"""
Crear una clase estudiante que tenga los atributos nombre, edad y grado. Ademas
de cargar un metodo que se llame estudiar que imprima el mensaje el estudiante 'nombre del
estudiante' esta estudiando, para trabajar con instancias estaria bueno que podamos
crear una instancia de esta clase y usar el metodo, pero para esto habria que generar
una interacion con el usuario osea debe ser un requerimiento, se tiene que pedir el nombre
edad y grado y a continuacion instanciar esta clase y mostrar los datos de la clase creada. Si
despues de registrar el estudiante el usuario escribe estudiar poner al estudiante a estudiar
indistinto de mayusculas o minusculas
"""

class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    
    def estudiar(self):
        print("Estudiando...")

nombre = input("Digame su nombre: ")
edad = input("Ahora su edad: ")
grado = input("Por ultimo, su grado: ")

estudiante = Estudiante(nombre, edad, grado)

print(f"""
      DATOS DEL ESTUDIANTE: \n\n
      Nombre: {estudiante.nombre} \n
      Edad: {estudiante.edad} \n
      Grado: {estudiante.grado} \n
      
    """)

while True:
    estudiar = input()
    if (estudiar.lower() == "estudiar"):
        estudiante.estudiar()
        break
"""
Salida:
Digame su nombre: Nestor
Ahora su edad: 20
Por ultimo, su grado: 5

      DATOS DEL ESTUDIANTE:


      Nombre: Nestor

      Edad: 20

      Grado: 5



estudiar
Estudiando...
"""