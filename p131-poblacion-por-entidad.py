import pandas as pd

#leer de un archivo delimitado los datos de la vivienda por estado
miserie = pd.read_csv('poblacion.csv',header =None, index_col = 0).squeeze(1)
miserie.name='poblacion'

#toda la serie
print('Trabajando con los datos de la serie completa \n')
print('orden original',miserie, '\n')
print('orden inverso',miserie[::-1], '\n')
print('orden ascendente por indice',miserie.sort_index(ascending=True), '\n')
print('orden descendente por valor',miserie.sort_values(ascending=False), '\n')

# atributos de la serie
print('los atributos de la serie \n')
print(f'Nombre: {miserie.name}, Tamano: {miserie.size}, Tipo: {miserie.dtype}, Bytes: {miserie.nbytes}, Tamano de dato: {miserie.nbytes//miserie.size}')

#iterar sobre los valores individuales de la serie
print('Iterando sobre los valores individuales de la serie \n')

for m,v in miserie.items():
    print(f'La entidad de: {m} tiene una poblacion de: {v}')

#acceso a datos por indice numerico
print('Ejemplos de acceso a datos por indice numerico \n')
print('Los primeros 5', miserie[:5], '\n')
print('Los ultimos 5', miserie[-5:], '\n')
print('Consecutivos ', miserie[4:9], '\n')
print('Salteados ', miserie[[5,10,15,20]], '\n')

#acceso a datos por indice alfabetico
print('Ejemplos de acceso a datos por indice alfabetico \n ')
print('Los primeros 5', miserie[:'Coahuila'], '\n')
print('Los ultimos 5', miserie['Tamaulipas':], '\n')
print('Consecutivos ', miserie['Aguascalientes':'Chiapas'], '\n')
print('Salteados ', miserie[['Guanajuato','Zacatecas','Sonora','Tabasco']], '\n')
print('los primeros 5 con head', miserie.head(5), '\n')
print('los ultimos 5 con tail', miserie.tail(5), '\n')
#filtrar datos
print('Ejemplos de filtrado de datos en serie \n')
print('los primeros 5 con head', miserie.head(5), '\n')
print('los ultimos 5 con tail', miserie.tail(5), '\n')
print('Valor >300', miserie[miserie>300], '\n')
print('Valor entre 300 y 1200 ordenados de menor a mayor', miserie[(miserie>=10)&(miserie<=100)].sort_values(), '\n')

#Estadisticas
print('Estadisticas descriptiva de los datos de la serie \n')
print('Resumen estadistico', miserie.describe())
print(f'Media: {miserie.mean()}, Desviacion: {miserie.std()}, Minimo: {miserie.min()}, Maximo: {miserie.max()}')
print(f'Q25:{miserie.quantile(q=0.25)} , Q50: {miserie.quantile(q=0.50)}, Q75: {miserie.quantile(q=0.75)}')
print('Moda', miserie.mode())

#Otras operaciones con los datos de la serie
print('La suma de todos   :',miserie.sum())
print('La suma de los primeros 10: ', miserie.head(10).sum())
print('la Desviacion salteados   : ', miserie[['Sonora','Tabasco','Zacatecas']].mean())
print('Modulo 15 a todos: ', miserie//15)
print('Sumar 20 a todos       :', miserie+20)