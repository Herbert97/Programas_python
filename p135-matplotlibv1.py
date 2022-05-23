from cProfile import label
import pandas as pd
import matplotlib.pyplot as plt
import os

os.system('cls')

fifa= pd.read_csv('players_21.csv')
print(fifa.shape)

#histograma/edad
#https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html

dg=fifa['age']
#print(dg)
plt.figure(figsize=(10,6))
plt.title('histograma de Edad')
plt.xlabel('edades')
plt.ylabel('numero de jugadores')
plt.hist(dg, color='green')
#plt.show()
plt.close()

#Barras/ valor en euros (5)
#https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html
#un grafico de barras es util para comprara una variable entre distintos grupos o categorias
dg= fifa[['short_name','value_eur']].sort_values(ascending=False, by='value_eur').iloc[0:15]
#print(dg)
plt.figure(figsize=(15,10))
plt.bar(dg.short_name, dg.value_eur)
plt.title('barras del valor en euros')
plt.xlabel('jugador')
plt.ylabel('valor en euros')
plt.tick_params(rotation=45)
plt.bar(dg.short_name,dg.value_eur,color='cyan',edgecolor='blue',hatch='/')
#plt.show()
plt.close()

#barras horizontal/jugadores por nacionalidad
#https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.barh.html
# un grafico de barras es util para comparar una variable entre distintos grupos o categorias

dg=fifa['nationality'].value_counts().sort_values(ascending=False).iloc[0:15]
#print(dg)
plt.figure(figsize=(10,8))
plt.title('jugadores por nacionalidad', fontsize=25)
plt.xlabel('No de jugadores')
plt.ylabel('Nacionalidad')
plt.barh(dg.index, dg.values, color=['red','blue'], edgecolor='black', hatch='/')
#plt.show()
plt.close()

#pastel/jugadores por club-salario en euros
# un grafico circular se usa para mostrar la relacion porcentual entre las partes con relacion a su conjunto
#https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.pie.html
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html


dg=fifa.groupby('club_name').sum()['wage_eur'].sort_values(ascending=False).head(8)
#print(dg)
plt.title('salario en Euros por Club')
plt.pie(dg.values, labels=dg.index, autopct='%1.0f%%', explode=(0.1,0.1,0,0,0,0,0,0), shadow=True)
plt.legend(dg.index, loc='best')
#plt.show()
plt.close()

# boxplot/rendimiento de los jugadores
# los diagramas de cajas son utiles para representar grupos de datos y compararlos entre ellos
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.boxplot.html


dg = fifa[fifa['club_name']=='FC Barcelona']['overall']
#print(dg)
plt.title('Rendimiento General de los Jugadores')
plt.ylabel('Rendimiento')
plt.boxplot(dg)
#plt.show()
plt.close()

#scatter/edad vs rendimiento
# el grafico de dispersion o scatter, sirve para representar la relacion entre dos variables
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html

dg= fifa[['age','overall']]
#print(dg.shape)
plt.title('Edad vs Rendimiento')
plt.xlabel('Edad')
plt.ylabel('Rendimiento')
plt.scatter(dg.age, dg.overall)
#plt.show()
plt.close()

# hexbin/Edad vs potencial
# muestra la relacion entre dos variables
#https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hexbin.html
dg= fifa[['age','potential']]
#print(dg.shape)
plt.title('Edad vs Potencial')
plt.xlabel('Edad')
plt.ylabel('Potencial')
plt.hexbin(dg.age,dg.potential, gridsize=30)
plt.colorbar()
#plt.show()
plt.close



