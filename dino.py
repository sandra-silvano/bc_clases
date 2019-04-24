class Dino:
    patas = 4
    nombre = None
    def __init__(self, canti_patas, un_nombre):
        self.patas = canti_patas
        self.nombre = un_nombre
        print("Hola soy un dinosaurio, me llamo", self.nombre, "y tengo", self.patas, "patas")
    
    def gte_patas(self):
        return self.patas
    
    def set_patas(self, cantidad):
        self.patas = cantidad

pepito = Dino(4, "Pepito")
