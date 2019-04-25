import requests
from pprint import pprint                 # Imprimi de una forma más linda: pretty print

API_KEY = "595695c3"
URL = "http://www.omdbapi.com/?apikey="
titulo = "Blade"
busqueda = URL + API_KEY + "&T=" + titulo
print(busqueda)

respuesta = requests.get(busqueda)
dic_peli = respuesta.json()
pprint(dic_peli)
print(dic_peli["Year"])

# Ejercicio 1
# Consultar el API de OMDB y obtener el nombre del director de Fight Club

import requests
from pprint import pprint                 # Imprimi de una forma más linda: pretty print

API_KEY = "595695c3"
URL = "http://www.omdbapi.com/?apikey="
titulo = "Fight Club"
busqueda = URL + API_KEY + "&T=" + titulo
print(busqueda)

respuesta = requests.get(busqueda)
dic_peli = respuesta.json()
pprint(dic_peli)
print(dic_peli["Director"])

# Ejercicio 2 
# Crear una funcion que reciba como argumento el titulo de una pelicula y 
# retorne los actores de esa pelicula


import requests
from pprint import pprint                 

def pelicula(titulo):
    API_KEY = "595695c3"
    URL = "http://www.omdbapi.com/?apikey="
    busqueda = URL + API_KEY + "&t=" + titulo
    respuesta = requests.get(busqueda)
    dic_peli = respuesta.json()
    print(dic_peli["Actors"])

pelicula("Star Wars")

 