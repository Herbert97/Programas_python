import pandas as pd
import matplotlib.pyplot as plt
import os 
import numpy as np

os.system('cls')

fifa = pd.read_csv('players_21.csv')

mc = fifa.query("club_name=='Manchester City'")
ch = fifa.query("club_name=='Chelsea'")
mi = fifa.query("club_name=='Milan'")
aj = fifa.query("club_name=='Ajax'")

#histograma
dg=fifa['height_cm']
#print(dg)
plt.figure(figsize=(10,6))
plt.title('histograma de altura')
plt.xlabel('altura')
plt.ylabel('numero de jugadores')
plt.hist(dg, color='cyan')
#plt.show()
plt.close()

#Barras
dg= fifa[['short_name','wage_eur']].sort_values(ascending=False, by='wage_eur').iloc[0:15]
#print(dg)
plt.figure(figsize=(15,10))
plt.bar(dg.short_name, dg.wage_eur)
plt.title('barras del valor en euros')
plt.xlabel('jugador')
plt.ylabel('valor en euros')
plt.tick_params(rotation=45)
plt.bar(dg.short_name,dg.wage_eur,color='green',edgecolor='red',hatch='/')
#plt.show()
plt.close()

#barras horizontal
dg=fifa['club_name'].value_counts().sort_values(ascending=False).iloc[0:15]
#print(dg)
plt.figure(figsize=(10,8))
plt.title('jugadores por club', fontsize=25)
plt.xlabel('No de jugadores')
plt.ylabel('Club')
plt.barh(dg.index, dg.values, color=['green','yellow'], edgecolor='blue', hatch='/')
#plt.show()
plt.close()

#pastel
dg=fifa.groupby('nationality').sum()['value_eur'].sort_values(ascending=False).head(10)
#print(dg)
plt.title('salario en Euros por Club')
plt.pie(dg.values, labels=dg.index, autopct='%1.0f%%', explode=(0.1,0.1,0,0,0,0,0,0,0,0), shadow=False)
plt.legend(dg.index, loc='best')
#plt.show()
plt.close()

# boxplot
dg = fifa[fifa['club_name']=='Milan']['weight_kg']
#print(dg)
plt.title('Peso general de los jugadores')
plt.ylabel('Peso')
plt.boxplot(dg)
#plt.show()
plt.close()

#scatter
dg= fifa[['height_cm','potential']]
#print(dg.shape)
plt.title('Estatura en cm vs Potencial')
plt.xlabel('Estatura')
plt.ylabel('Potencial')
plt.scatter(dg.height_cm, dg.potential)
#plt.show()
plt.close()

# hexbin
dg= aj[['potential','weight_kg']]
#print(dg.shape)
plt.title('Potencial vs Peso en Kg del club Ajax')
plt.xlabel('Potencial')
plt.ylabel('Peso en kg')
plt.hexbin(dg.potential,dg.weight_kg, gridsize=30)
plt.colorbar()
#plt.show()
plt.close

# Gráficas cara a cara misma figura
plt.figure(figsize=(10,8))
plt.title('Histograma de Peso')
plt.xlabel('Peso')
plt.ylabel('Número de Jugadores')
plt.hist(ch.age, color='cyan', density=False, label='CH')
plt.hist(aj.age, color='red', density=False, label='AJ')
plt.hist(mc.age, color='green', density=False, label='MC')
plt.legend(loc='upper right')
#plt.savefig('histograma.png')
#plt.show()
plt.close() 

# Barras / Jugadores mas valiosos
dgch = ch['value_eur'].sort_values(ascending=False).iloc[0:5]
dgmc = mc['value_eur'].sort_values(ascending=False).iloc[0:5]
dgaj = aj['value_eur'].sort_values(ascending=False).iloc[0:5]

n = dgch.shape[0]
sp = np.arange(n)
w = 0.3

plt.figure(figsize=(10,8))
plt.title('Valor en Euros')
plt.xlabel('Jugador')
plt.ylabel('Valor Euros')
plt.bar(sp, dgch, w, color='red', edgecolor='black', label='CH')
plt.bar(sp + w, dgmc, w, color='blue', edgecolor='orange', label='MC')
plt.bar(sp + w, dgaj, w, color='green', edgecolor='cyan', label='AJ')
plt.legend()
plt.xticks(sp,['Jugador 1','Jugador 2','Jugador 3','Jugador 4','Jugador 5'])
#plt.show()
plt.close()

# Boxplot / Rendimento 
plt.figure(figsize=(10,8))
plt.title('Potencial General de los Jugadores')
plt.ylabel('Potencial')
sp = np.arange(2)
dg = [ch.potential, aj.potential, mc.potential]
plt.boxplot(dg, labels=['CH','AJ','MC'])
#plt.show()
plt.close()

# Poner graficas en un plot diferente box

# Pie / Jugadores por País

dgrm = ch.preferred_foot.value_counts()
dgbr = mc.preferred_foot.value_counts()
dgjv = mi.preferred_foot.value_counts()
#print(dgrm, dgbr, dgjv)

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(12,6))
fig.suptitle('Jugadores por País')
plt.subplots_adjust( wspace=0.3 )
ax1.title.set_text('Chelsea')
ax1.pie(labels=dgrm.index, x=dgrm.values, autopct='%1.0f%%', startangle=90, shadow=True)
ax2.title.set_text('Manchester City')
ax2.pie(labels=dgbr.index, x=dgbr.values, autopct='%1.0f%%', startangle=90, shadow=True)
ax3.title.set_text('Milan')
ax3.pie(labels=dgjv.index, x=dgjv.values, autopct='%1.0f%%', startangle=90, shadow=True)
#plt.show()
plt.close()

# scatter - Edad vs rendimiento  
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html

fig, ax = plt.subplots(2,2, constrained_layout=True, figsize=(10,8))
fig.suptitle('Peso vs potencial', size=18)
#fig.supxlabel('Peso')
#fig.supylabel('Potencial')
ax[0,0].set_title('Manchester City')
ax[0,0].scatter(mc.weight_kg, mc.potential)
ax[0,1].set_title('Chelsea')
ax[0,1].scatter(ch.weight_kg, ch.potential)
ax[1,0].set_title('Milan')
ax[1,0].scatter(mi.weight_kg, mi.potential) 
ax[1,1].set_title('Ajax')
ax[1,1].scatter(aj.weight_kg, aj.potential)
#plt.show()
plt.close()

# hexbin / Edad vs Potencial

fig = plt.figure(figsize=(10,8))
fig.suptitle('Goleo vs aceleracion de movimiento')

ax1 = fig.add_subplot(2,2,1)
ax1.set_title('Manchester City')
im1 = ax1.hexbin(mc.attacking_finishing,mc.movement_acceleration, cmap="Blues", gridsize=20)
fig.colorbar(im1)

ax2 = fig.add_subplot(2,2,2)
ax2.set_title('Chelsea')
im2 = ax2.hexbin(ch.attacking_finishing,ch.movement_acceleration, cmap="Greens", gridsize=20)
fig.colorbar(im2)

ax3 = fig.add_subplot(2,2,3)
ax3.set_title('Milan')
im3 = ax3.hexbin(mi.attacking_finishing,mi.movement_acceleration, cmap="Purples", gridsize=20)
fig.colorbar(im3)

ax4 = fig.add_subplot(2,2,4)
ax4.set_title('Ajax')
im4 = ax4.hexbin(aj.attacking_finishing,aj.movement_acceleration, cmap="Oranges", gridsize=20)
fig.colorbar(im4)

plt.show()
plt.close()