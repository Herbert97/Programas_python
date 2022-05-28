import pandas as pd
edades = {"Juan":40, "Pedro":20, "Maria":36, "Francisco":20, "Luis":34}
datos = pd.Series(edades)
datos.name = 'Edades'
print(datos.name) # nombre

print(datos.dtype) # tipos de datos

print(datos.size) # número de elemenos

print(datos.index) # etiquetas o indices

print(datos.values) # valores de la serie