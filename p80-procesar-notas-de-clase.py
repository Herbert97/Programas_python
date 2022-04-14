#procesar notas de clase
print('Introduce calificaciones entre 0 y 10 (100 para terminar):')
nums=[]
n=0
while n!=100:
    n = float(input("dame la calificacion > "))
    if n>=0 and n<=10:
        nums.append(n)
    else:
        print('no se encuentra dentro del rango')
print('FIN')            

suma=0
for n in nums:
    suma=suma+n
promedio= suma/len(nums)

mp=[]
for n in nums:
    if n>promedio:
        mp.append(n)

may=nums[0]
for n in nums:
    if n> may:
        nums.append(n)
men=nums[0]
for n in nums:
    if n < men:
        men=n
print(f'se capturaron {len(nums)} calificaciones estas son: {nums}')
print('\n Estadisticas')
print(f'la suma es : {suma}')
print(f'el promedio: {promedio}')
print(f'mayores al promedio: {len(mp)}: {mp}')
print(f'el Mayor es : {may} ')
print(f'el menor es: {men} ')