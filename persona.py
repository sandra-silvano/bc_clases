# Ejercicio

# En el archivo persona.py crear una clase Persona con atributo nombre. 
# Después instanciar un objeto de tipo persona

class Persona:
    nombre = None
    def __init__(self, un_nombre):
        self.nombre = un_nombre
        print("Soy una persona que se llama", self.nombre,)

Pepito = Persona("Caesar")
Pepita = Persona("Nico")



