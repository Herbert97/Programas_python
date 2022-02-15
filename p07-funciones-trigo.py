# uso de  las funciones trigonometicas en python
import math 

print('calculando funciones trignometricas...')
angulogrados = int(input('Dame el angulo el grados'))
angulo = math.radians(angulogrados) #convierte grados a radianes
seno = math.sin(angulo)
coseno = math.cos(angulo)
tangente= math.tan(angulo)
print(f'seno: {seno}, coseno: {coseno}, tangente: {tangente}')