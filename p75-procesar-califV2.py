# Entrada
print('Introduce calificaciones 0..9 (99 para terminar):')
nums=[]
n=0
while n!=99:
    n = float(input("dame la calificacion > "))
    if n>=0 and n<=10:
        nums.append(n)
    else:
        print('X')
print('FIN')            

suma=sum(nums)
promedio= suma/len(nums)

mp=[n for n in nums if n>promedio]

mayo=max(nums)
men=min(nums)
may=nums[0]

print(f'capturaste {len(nums)}: {nums}')
print('\n Estadisticas')
print(f'la suma es : {suma}')
print(f'el promedio: {promedio}')
print(f'mayores al promedio: {len(mp)}: {mp}')
print(f'el Mayor es : {may}')
print(f'el menor es: {men}')