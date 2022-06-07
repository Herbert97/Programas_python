import pandas as pd
import os

os.system('cls')

# 1. importar los datos del arcihvo csv
fifa21=pd.read_csv('players_21.csv')

#2 el dataframe original
print('todo el dataframe: \n\n', fifa21, '\n')
print('Forma            : ',fifa21.shape,'\n')
print('tamaño           : ',fifa21.size,'\n')
print('Columnas         : ',fifa21.columns,'\n')

# 3 el DataFrame de reducido

fifa21small=fifa21[['short_name', 'age', 'height_cm', 'weight_kg', 'nationality', 'club_name',
'overall', 'potential', 'value_eur', 'wage_eur', 'player_positions', 'preferred_foot', 'shooting', 'passing',
'dribbling', 'defending', 'mentality_aggression', 'mentality_interceptions', 'mentality_positioning']]

fifasm=fifa21small[(fifa21small['club_name']=='Liverpool') | (fifa21small['club_name']=='Juventus') | (fifa21small['club_name']=='Chelsea')]

fifasm.set_index('short_name',inplace=True)

print('Orden original: \n', fifasm, '\n')
print('Orden inverso: \n', fifasm[::-1], '\n')
print('Orden ascendente por indice', fifasm.sort_index(ascending=True), '\n')
print('orden ascendente por nacionalidad', fifasm.sort_values(ascending=True, by='nationality'), '\n')
print('Forma            : ',fifasm.shape,'\n')
print('tamaño           : ',fifasm.size,'\n')
print('Columnas         : ',fifasm.columns,'\n')
print('Tipos            :\n\n', fifasm.dtypes, '\n')

#4 iterar sobre el DataFrame
print('\n Iterar sobre el Dataframe')

print('Iterar por columnas: ')
for c,s in fifasm.items():
    print('\nColumna: ',c,'\n')
    print('Serie: \n',s)

print('\n Iterar por los rengoles y las columnas v1: ')
print('Estatura, peso y nacionalidad: \n')
for i,r in fifasm.iterrows():
    print(i,'mide',r['height_cm'],'cm y pesa',r['weight_kg'],'kg','es de nacionalidad',r['nationality'])    

print('\nIterar por renglones y columnas v2')
for r in fifasm.itertuples():
    print(r,'\n')

#5 acceder a una serie del DataFrame
print('\nAccerder una serie por indice alfabetico o nombre \n')
print('Serie defending                   :', fifasm['defending'].sort_values(ascending=False), '\n')
print('Serie passing              :\n', fifasm.passing.sort_values(ascending=False),'\n')
print('los primeros 10, todas las series:\n',fifasm.head(10),'\n')
print('los ultimos 10, todas las series :\n', fifasm.tail(10),'\n')
print('Acceder al tope y cola de una serie especifica:\n')
print('primeros 10 de una serie          :\n\n',fifasm['weight_kg'].head(10),'\n')
print('Ultimos 10 de una serie           :\n',fifasm.value_eur.tail(10),'\n')

#6 acceder por indice numérico
print('\nAcceder por indice numérico: \n\n')
print('\nAccceder renglones usando indice numérico: \n')
print('Acceder renglon :\n',fifasm.iloc[5])
print('\nAcceder renglones continuos: \n')
print(fifasm.iloc[5:10])
print('\nAcceder renglones dispersos:\n')
print(fifasm.iloc[[2,4,6]])
print('\nAcceder renglones alternados \n')
print(fifasm.iloc[1:15:2])

print('\nAccceder columnas usando indice numérico: \n')
print('Acceder columna :\n')
print(fifasm.iloc[:,1])
print('\nAcceder columnas continuas: \n')
print(fifasm.iloc[:,1:5])
print('\nAcceder columnas dispersas:\n')
print(fifasm.iloc[:,[3,5,7]])
print('\nAcceder columnas alternadas \n')
print(fifasm.iloc[:,6:10:2])

#7 acceder por indice alfabetico
print('\nAcceder renglones por indice alfabético: \n')
print('\n acceder renglon \n')
#print(fifasm.loc['Marcelo'])
print('\nAcceder renglones continuos: \n')
print(fifasm.loc['C. Jones':'C. Kelleher'])
print('\nAcceder a renglones dispersos \n')
print(fifasm.loc[['Alisson','G. Frabotta','L. Coccolo']])
print('\nacceder renglones alternados: \n')
print(fifasm.loc['Cristiano Ronaldo': 'C. Kelleher':2])

print('\nAcceder Columnas por indice alfabético: \n')
print('\nAcceder columna especifica \n')
print(fifasm.loc[:,'mentality_interceptions'])
print('\nacceder columnas consecutivas')
print(fifasm.loc[:,'age':'nationality'])
print('\nAcceder columnas disperas')
print(fifasm.loc[:,['shooting','passing','overall']])
print('\nAcceder columnas alternadas')
print(fifasm.loc[:,'age':'defending':2])

# 8 Acceder a un elemento

print('\n Acceder Elemento: \n')

print(fifasm)
print('\nAcceder elemento por indice numérico: \n')
print('Primer renglon y primera columna: ', fifasm.iat[0,0])
print('Ultimo renglon y ultima columna: ',fifasm.iat[96,17])
print('\nAcceder elemento por indice alfabético: \n')
print('Primer renglon y primera columna: ',fifasm.at['Cristiano Ronaldo','age'])
print('Ultimo renglon y ultima columna: ', fifasm.at['C. Kelleher','mentality_positioning'])

#9 filtrar datos v1

print('\n filtrar datos v1: \n')

print('\nFiltar por un criterio ejemplo 1 \n')
print( fifasm[fifasm['age']>=35])
print('\nFiltrar por un criterio ejemplo 2\n')
print(fifasm[fifasm.player_positions.isin(['CB','ST']) ] )
print('\n Filtar por un criterio ejemplo3\n')
print( fifasm[fifasm['nationality'].str.startswith('B') ] )
print('\n Filtrar por dos criterios \n')
print( fifasm[ (fifasm['age']<=20) & (fifasm['club_name']=='Juventus') ] )

#10 filtrar datos V2
print('\n filtrar  datos v3: \n')

print('\n filtrar por un criterio ejemplo 1 \n')
print(fifasm.query('age>=30 '))
print('\nfiltrar por un cirterio ejemplo2 \n')
print(fifasm.query("nationality != 'Spain' ")['nationality'])
print('\n Filtrar por un criterio ejemplo 3\n ')
print(fifasm.query(" nationality in ('Sweden','Brazil')")['nationality'])
print('\n filtrar por dos criterios ejemplo1 \n')
print(fifasm.query(" shooting>= 49 & shooting<=89 ")[['shooting']])
print('\n Filtrar por dos criterios ejemplo 2\n')
print(fifasm.query("mentality_aggression < 40 & 'club_name'== 'Juventus'"))
print('\nFiltrar por dos criterios ejemplo 3 \n')
print(fifasm.query(" nationality not in ('Brazil','Peru') & passing<79")[['passing','nationality']] )

#11 estadistica descriptiva
print('\n Estadistica descriptiva: \n')

print('Estadistica descriptiva general: \n')
print(fifasm.describe())
print('\nEstadistica descriptiva individual \n')
print('La cuenta            :', fifasm.count(),'\n')
print('La Media             :', fifasm.mean(numeric_only=True),'\n')
print('La Desviacion        :', fifasm.std(numeric_only=True),'\n')
print('El minimo            :', fifasm.min(numeric_only=True),'\n')
print('El maximo            :', fifasm.max(numeric_only=True),'\n')
print('Q 25%                :', fifasm.quantile(q=0.25),'\n')
print('\n Estadistica descriptiva de una Serie: \n')
print(fifasm['passing'].describe(), '\n')
print(fifasm.shooting.describe(),'\n')

# 12 Agrupar datos
print('\n Agrupar datos \n')

print('\n Agrupar por columna ejemplo 1:')
print(fifasm.groupby('passing').sum().sort_values(ascending=False, by='passing'))
print('\n Agrupar por columna ejemplo 2: ')
print(fifasm.groupby('shooting').mean())
print('\nAgrupar por dos columnas: ')
print(fifasm.groupby(['club_name'])[['nationality']].sum)

# 13 Operaciones entre Series
print('\n Operaciones entre Series')

print('\n Suma de mentality_interceptions y mentality_positioning y mentality_aggression')
print(fifasm.eval('suma=(mentality_interceptions+mentality_positioning+mentality_aggression)'))
print('\n Con dribbling mayor igual a 70 , expresion Boleana')
print(fifasm.eval('dribbling>=70'))
print('\n Con peso mayor al peso promedio', fifasm.defending.mean())
print(fifasm.eval('defending >= defending.mean()'))