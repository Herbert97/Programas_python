import pandas as pd
edades = {"Juan":40, "Pedro":20, "Maria":36, "Francisco":20, "Luis":34}
datos = pd.Series(edades)
datos.name = 'Edades'

# estadistica descriptiva
print( datos.describe(), '\n')

print( datos.count() ) # Cuenta

print( datos.mean() ) # Media

print( datos.std() ) # Desv estandar

print( datos.min() ) # Minimo

print( datos.quantile(q=0.25) ) # Quartil 25%

print( datos.quantile(q=0.50) ) # Quartil 50%

print( datos.quantile(q=0.75) ) # Quartil 75%

print( datos.max() ) # Maximo

print( datos.mode() ) # Moda