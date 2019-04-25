import requests
URL = 
respuesta = requests.get(URL)
texto = respuesta.text
print(respuesta)
print(texto)
print(len(texto))

cotizacion = respuesta.json()
print(cotizacion)
print(len(texto))
print(type(cotizacion))


dolar_compra = cotizacion["dolarpy"]["set"]["compra"]
print("El dolar está a", dolar_compra, "guaranies")

precio_corolla = 20000

precio_giaranies = dolar_compra * precio_corolla
print("El corolla cuesta", precio_guaranies, "guaranies")

