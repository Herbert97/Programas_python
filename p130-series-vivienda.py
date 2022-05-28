import pandas as pd

#leer de un archivo delimitado los datos de la vivienda por estado
miserie = pd.read_csv('vivienda.csv',header =None, index_col = 0).squeeze(1)
miserie.name='vivienda'

#toda la serie
print('Trabajando con los datos de la serie completa \n')
print('orden original',miserie, '\n')

print('orden inverso',miserie[::-1], '\n')

print('orden ascendente por indice',miserie.sort_index(ascending=True), '\n')

print('orden descendente por indice',miserie.sort_values(ascending=False), '\n')

# atributos de la serie
print('los atributos de la serie \n')
print(f'Nombre: {miserie.name}, Tamano: {miserie.size}, Tipo: {miserie.dtype}, Bytes: {miserie.nbytes}, Tamano de dato: {miserie.nbytes//miserie.size}')

#iterar sobre los valores individuales de la serie
print('Iterando sobre los valores individuales de la serie \n')

for m,v in miserie.items():
    print(f'El municipio de {m} tiene un total de {v} viviendas')

#acceso a datos por indice numerico
print('Ejemplos de acceso a datos por indice numerico \n')
print('Los primeros 5', miserie[:5], '\n')
print('Los ultimos 5', miserie[-5:], '\n')
print('Consecutivos ', miserie[4:9], '\n')
print('Salteados ', miserie[[5,10,15,20]], '\n')

#acceso a datos por indice alfabetico
print('Ejemplos de acceso a datos por indice alfabetico \n ')
print('Los primeros 5', miserie[:'Calera'], '\n')
print('Los ultimos 5', miserie['Villa Hidalgo':], '\n')
print('Consecutivos ', miserie['Jalpa':'Loreto'], '\n')
print('Salteados ', miserie[['Jerez','Fresnillo','Calera','Pinos']], '\n')

#filtrar datos
print('Ejemplos de filtrado de datos en serie \n')
print('los primeros 5', miserie.head(5), '\n')
print('los ultimos 5', miserie.tail(5), '\n')
print('Valor >5000', miserie[miserie>5000], '\n')
print('Valor >5000 ordenados de mayor a menor', miserie[miserie>5000].sort_values(ascending=False), '\n')
print('Valor entre 300 y 1200 ordenados de menor a mayor', miserie[(miserie>=300)&(miserie<=1200)].sort_values(), '\n')

#Estadisticas
print('Estadisticas descriptiva de los datos de la serie \n')
print('Resumen estadistico', miserie.describe())
print(f'Media: {miserie.mean()}, Desviacion: {miserie.std()}, Minimo: {miserie.min()}, Maximo: {miserie.max()}')
print(f'Q25:{miserie.quantile(q=0.25)} , Q50: {miserie.quantile(q=0.50)}, Q75: {miserie.quantile(q=0.75)}')
print('Moda', miserie.mode())

#Otras operaciones con los datos de la serie
print('La suma de todos   :',miserie.sum())
print('La suma de los primeros 10: ', miserie.head(10).sum())
print('La media de los ultimos 10: ', miserie.tail(10).mean())
print('la Desviacion salteados   : ', miserie[['Calera','Fresnillo','Apulco']].std())
print('Incremento del 10%       :', miserie*0.1)

datosconel10=miserie*0.1
datosconel10.to_csv('Vviviendas10.csv')
