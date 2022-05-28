import pandas as pd

indice = ['Juan', 'Pedro', 'Maria', 'Francisco', 'Luis']
valores = [40, 20, 36, 20, 34]
datos = pd.Series(valores, indice)
datos.name = 'Edades'
print(datos)