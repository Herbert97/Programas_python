import pandas as pd
edades = {"Juan":40, "Pedro":20, "Maria":36, "Francisco":20, "Luis":34}
datos = pd.Series(edades)
datos.name = 'Edades'
# edad de juan
print(datos[0], '\n')

# Los 3 primeros (indices 0,1,2)
print(datos[:3], '\n')

#los 3 ultimos (indices 2,3,4 )
print(datos[-3:], '\n')

# elementos consecutivos (indice 1,2,3)
print(datos[1:4], '\n')

# elementos no consecutivos (indice 1 y 4)
print(datos[[1,4]], '\n')

# acceder a elementos en orden inverso'
print(datos[::-1], '\n')