#listas aleatiorios suma, dos listas de 10 numeros aleatorios y genera una suma.
import random


l1 = []
l2 = []
c=10
print('generando listas')
for n in range(c):
    l1.append(random.randint(1,100))
    l2.append(random.randint(1,100))   
print("\nListas originales:")
print(f"Lista 1 : {l1}")
print(f"Lista 2 : {l2}")

l3=[]
for n in range(c):
    if l1[n]%2 and l2[n]%2 !=0:
        l3.append(l1[n]+l2[n])
print(f'la suma es de los impares {l3}')