# Ejercicio

# En el archivo persona.py crear una clase Persona con atributo nombre. 
# Después instanciar un objeto de tipo persona

class Persona:
    nombre = None
    edad = 27
    def __init__(self, un_nombre, cumple):
        self.nombre = un_nombre
        self.edad = cumple
        print("Me llamo", self.nombre,"y tengo", self.edad, "años")
    
    def get_edad(self):
        return self.edad
    
    def set_edad(self, cantidad):
        self.edad = cantidad

    def cumpleaños(self):
        self.edad = self.edad + 1
        print("Me llamo", self.nombre,"y tengo", self.edad, "años")

Individuo = Persona("Caesar", 27)

# Modificar la clase Persona, agregarle un atributo edad 
# y un método cumpleaños y un método get_edad
# Inicializar/crear un objeto de tipo Persona y hacerle cumplir años




