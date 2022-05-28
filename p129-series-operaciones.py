import pandas as pd
edades = {"Juan":40, "Pedro":20, "Maria":36, "Francisco":20, "Luis":34}
datos = pd.Series(edades)
datos.name = 'Edades'

print( datos.sum(), '\n') # la suma de todas las edades

print( datos[0:3].sum(), '\n') # suma edades de 0 a 3

print( datos[['Juan','Pedro']].sum(), '\n') # suma edades Juan y Pedro

print( datos['Pedro':'Francisco'].sum(), '\n') # suma edades Juan y Pedro

print( datos[[0,2,4]].mean(), '\n') # media de indices 0,2,4

print( datos[2:4].std(), '\n') # desvacion de indices 2,3

print( datos+3, '\n') # suma 3 a todas las edades

print( datos*2, '\n') # multiplica x 2 todas las edades