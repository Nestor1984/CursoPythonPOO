"""
Metodo: es una accion que un objeto puede realizar.
"""
class Celular:
    
    # Metodo Constructor
    def __init__(self, marca, modelo, camara): # Declaramos el parametro self y los otros 3 parametros que vamos a necesitar
        # Atributos
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
        
    # Metodos
    def llamar(self):
        print(f'Estas haciendo un llamado desde un: {self.modelo}')
            
    def cortar(self):
        print(f'Cortaste la llamada desde tu: {self.modelo}')

# Creamos un primer objeto       
celular1 = Celular("Samsung", "S23", "48MP") # Le enviamos los 3 argumentos que nos piden (nos olvidamos del self)
# Creamos un segundo objeto 
celular2 = Celular("Apple", "Iphone 15 Pro", "96MP") # Le enviamos los 3 argumentos que nos piden (nos olvidamos del self)

# Invocamos a los metodos
celular1.llamar()
celular1.cortar()
print()
celular2.llamar()
celular2.cortar()

"""
Salida:
Estas haciendo un llamado desde un: S23
Cortaste la llamada desde tu: S23

Estas haciendo un llamado desde un: Iphone 15 Pro
Cortaste la llamada desde tu: Iphone 15 Pro      
"""