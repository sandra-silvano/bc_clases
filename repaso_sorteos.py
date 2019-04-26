
# Sorteo para 5 personas, hay 3 premios
# OJO: una persona no puede ganar 2 veces

# Solución 1

from random import randint
participantes = ["pepito", "pepita", "Nico", "Caesar", "Pame"]

for sorteo in range(3):
    ganador = participantes[randint(0,len(participantes)-1)]
    print("El ganador es", ganador)
    participantes.remove(ganador)

# Solución 2

from random import randint
participantes = ["pepito", "Nemo", "RoDi", "Dino", "GRShits"]
contador = 1

while contador <= 3:
    canti_ele = len(participantes) - 1
    ganador = participantes[randint(0, canti_ele)]
    print("El premio", contador, "es para", ganador)
    contador = contador + 1
    participantes.remove(ganador)

# Solución 3

from random import randint
participantes = ["pepito", "Nemo", "RoDi", "Dino", "GRShits"]
for sorteo in range(3):
    ganador = participantes[randint(0, len(participantes) - 1)]
    print("Ganador", sorteo + 1, ":", ganador)
    participantes.remove(ganador)








    
    






    
     