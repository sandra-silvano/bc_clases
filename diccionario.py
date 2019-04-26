'''diccionario = {}

nombre_de_diccionario = {"nombre_clave":"valor"}
# Lista
personalist = ["Marce", 32, "Programador"]
print(dic_persona)

# Diccionario
dic_persona = {"nombre": "Marce", "edad":32}
print(dic_persona["edad"])

dic_persona["edad"] = "mm cuanto me pones?"
print(dic_persona["edad"])
print(personalista[1])

dic_persona["profesion"] = "Programador"
print(dic_persona)

print(dic_persona.get("estatura")) '''

# Crear un diccionario persona con claves nombre, edad, estatura 
# e imprimir cada uno de los valores de las claves en un print diferente

# Luego cambiar la edad a otro valor e imprimir de nuevo
# Luego solicitar que se cambie la edad con input

# Luego agregar un par clave "hobby" que contenga 
# una lista de hobbies e imprimir todo el diccionario

persona = {"nombre": "Nico", "edad": 16, "estatura":1.61}
print(persona["nombre"])
print(persona["edad"])
print(persona["estatura"])


persona["edad"] = 18
print(persona["edad"])

persona["edad"] = input("Tengo  ")
print(persona)

persona["hobbies"]  = ["escuchar musica", "ver anime","cantar mientras lava los cubiertos"]
print(persona)

print(persona["hobbies"][2])
