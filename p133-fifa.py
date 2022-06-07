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

fifa21small=fifa21[['short_name','age','height_cm','weight_kg','nationality','club_name','overall','potential','value_eur','wage_eur','player_positions','power_jumping','power_long_shots']]

fifasm=fifa21small[(fifa21small['club_name']=='Real Madrid') | (fifa21small['club_name']=='FC Barcelona')]

fifasm.set_index('short_name',inplace=True)

print('Orden original: \n', fifasm, '\n')
print('Orden inverso: \n', fifasm[::-1], '\n')
print('Orden ascendente por indice', fifasm.sort_index(ascending=True), '\n')
print('orden descendente por valor', fifasm.sort_values(ascending=False, by='age'), '\n')
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
print('valor en euros                   :', fifasm['value_eur'].sort_values(ascending=False), '\n')
print('Rendimiento general              :\n', fifasm.overall.sort_values(ascending=False),'\n')
print('los primeros 10, todas las series:\n',fifasm.head(10),'\n')
print('los ultimos 10, todas las series :\n', fifasm.tail(10),'\n')
print('Acceder al tope y cola de una serie especifica:\n')
print('primeros 10 de una serie          :\n\n',fifasm['age'].head(10),'\n')
print('Ultimos 10 de una serie           :\n',fifasm.wage_eur.tail(10),'\n')

#6 acceder por indice numérico
print('\nAcceder por indice numérico: \n\n')
print('\nAccceder renglones usando indice numérico: \n')
print('Acceder renglon :\n',fifasm.iloc[3])
print('\nAcceder renglones continuos: \n')
print(fifasm.iloc[2:5])
print('\nAcceder renglones dispersos:\n')
print(fifasm.iloc[[1,3,5]])
print('\nAcceder renglones alternados \n')
print(fifasm.iloc[0:10:2])

print('\nAccceder columnas usando indice numérico: \n')
print('Acceder columna :\n')
print(fifasm.iloc[:,0])
print('\nAcceder columnas continuas: \n')
print(fifasm.iloc[:,0:3])
print('\nAcceder columnas dispersas:\n')
print(fifasm.iloc[:,[0,3]])
print('\nAcceder columnas alternadas \n')
print(fifasm.iloc[:,0:6:2])

#7 acceder por indice alfabetico
print('\nAcceder renglones por indice alfabético: \n')
print('\n acceder renglon \n')
print(fifasm.loc['Marcelo'])
print('\nAcceder renglones continuos: \n')
print(fifasm.loc['Casemiro':'Carvajal'])
print('\nAcceder a renglones dispersos \n')
print(fifasm.loc[['Isco','Mariano','Belman']])
print('\nacceder renglones alternados: \n')
print(fifasm.loc['T. Courtois': 'Marcelo':2])

print('\nAcceder Columnas por indice alfabético: \n')
print('\nAcceder columna especifica \n')
print(fifasm.loc[:,'age'])
print('\nacceder columnas consecutivas')
print(fifasm.loc[:,'age':'club_name'])
print('\nAcceder columbnas disperas')
print(fifasm.loc[:,['power_jumping','age','overall']])
print('\nAcceder columnas alternadas')
print(fifasm.loc[:,'age':'club_name':2])

# 8 Acceder a un elemento

print('\n Acceder Elemento: \n')

print(fifasm)
print('\nAcceder elemento por indice numérico: \n')
print('Primer renglon y primera columna: ', fifasm.iat[0,0])
print('Ultimo rengon y ultima columna: ',fifasm.iat[64,11])
print('\nAcceder elemento por indice alfabético: \n')
print('Primer renglon y primera columna: ',fifasm.at['L. Messi','age'])
print('Ultimo renglon y ultima columna: ', fifasm.at['Arribas','power_long_shots'])

#9 filtrar datos v1

print('\n filtrar datos v1: \n')

print('\nFiltar por un criterio ejemplo 1 \n')
print( fifasm[fifasm['age']>30])
print('\nFiltrar por un criterio ejemplo 2\n')
print(fifasm[fifasm.player_positions.isin(['LW','ST']) ] )
print('\n Filtar por un criterio ejemplo3\n')
print( fifasm[fifasm['nationality'].str.startswith('B') ] )
print('\n Filtrar por dos criterios \n')
print( fifasm[ (fifasm['age']<30) & (fifasm['club_name']=='FC Barcelona') ] )

#10 filtrar datos V2
print('\n filtrar  datos v3: \n')

print('\n filtrar por un criterio ejemplo 1 \n')
print(fifasm.query('age>=30 '))
print('\nfiltrar por un cirterio ejemplo2 \n')
print(fifasm.query("nationality != 'Brazil' ")['nationality'])
print('\n Filtrar por un criterio ejemplo 3\n ')
print(fifasm.query(" nationality in ('spain','Brazil')")['nationality'])
print('\n filtrar por dos criterios ejemplo1 \n')
print(fifasm.query(" age<= 30 & nationality== 'Spain' ")[['age','nationality']])
print('\n Filtrar por dos criterios ejemplo 2\n')
print(fifasm.query("weight_kg <= 80 & height_cm >= 180"))
print('\nFiltrar por dos criterios ejemplo 3 \n')
print(fifasm.query(" nationality not in ('Spain','Portugal')& age<=25")[['age','nationality']] )

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
print(fifasm['age'].describe(), '\n')
print(fifasm.height_cm.describe(),'v')

# 12 Agrupar datos
print('\n Agrupar datos \n')

print('\n Agrupar por columna ejemplo 1:')
print(fifasm.groupby('nationality')[['wage_eur','value_eur']].sum().sort_values(ascending=False, by='wage_eur'))
print('\n Agrupar por columna ejemplo 2: ')
print(fifasm.groupby('nationality').mean())
print('\nAgrupar por dos columnas: ')
print(fifasm.groupby(['club_name','nationality'])[['wage_eur','value_eur']].sum)

# 13 Operaciones entre Series
print('\n Operaciones entre Series')

print('\n Suma de Edad y Peso')
print(fifasm.eval('suma=(age+weight_kg)-height_cm'))
print('\n Con peso mayor igual a 70 , expresion Boleana')
print(fifasm.eval('weight_kg>=70'))
print('\n Con peso mayor al peso promedio', fifasm.weight_kg.mean())
print(fifasm.eval('weight_kg >= weight_kg.mean()'))