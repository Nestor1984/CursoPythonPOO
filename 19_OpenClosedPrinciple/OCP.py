"""
El principio Open/Closed (OCP), traducido como "Principio de Abierto/Cerrado", es otro principio fundamental en la POO
y el diseno de software.
El principio OCP establece lo siguiente: las entidades de software (como clases, modulos, funciones, etc.) deben estar
abiertas para la extension pero cerradas para la modificacion. Esto significa que una vez que una entidad de software ha
sido implementada y esta funcionando correctamente, no debe ser modificada directamente para cambiar su comportamiento. En
cambio, el comportamiento debe poder ser extendido sin necesidad de modificar el codigo existente.
Para cumplir con el principio OCP, se utiliza el mecanismo de la herencia, la composicion u otras tecnicas de extension. Por ejemplo:
Herencia: Se puede extender el comportamiento de una clase creando subclases que sobrescriban metodos o anadan nuevos metodos
sin modificar el codigo original.
Composicion: Se pueden utilizar interfaces, clases abstractas o patrones de diseno como el patron Strategy para permitir que el
comportamiento de un objeto pueda ser intercambiado o extendido sin alterar su codigo base.
"""

class Notificador:
    def __init__(self, usuario, mensaje): # Recibimos un objeto usuario de tipo Usuario (Esta clase no esta definida)
        self.usuario = usuario
        self.mensaje = mensaje
        
    def notificar(self):
        """
        NOTA: raise NotImplementedError es una sentencia que se utiliza para indicar que un metodo en una clase base (o superclase)
        es abstracto y debe ser implementado en las clases hijas (o subclases).
        """
        raise NotImplementedError 
    
class NotificadorEmail(Notificador):
    def notificar(self):
        print(f"Enviando mensaje por MAIL a {self.usuario.email}")
    
class NotificadorSMS(Notificador):
    def notificar(self):
        print(f"Enviando SMS a {self.usuario.sms}")

class NotificadorWhatsApp(Notificador):
    def notificar(self):
        print(f"Enviando Whatsapp a {self.usuario.whatsapp}")
        
class NotificadorTwitter(Notificador):
    def notificar(self):
        print(f"Enviando twit a {self.usuario.twitter}")
        
# Salida: Sin salida