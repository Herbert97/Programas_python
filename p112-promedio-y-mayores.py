# Promedio y mayores que el promedio
def promedio(lista):
    s = 0
    for n in lista:
        s += n
    return s / len(lista)

def maypresprom(lista, prom):
    mp = []
    for n in lista:
        if n > prom:
            mp.append(n)
    return mp

def leerdatos():
    datos=[]
    while True:
        d=int(input("número: "))
        if d==-1:
            break
        datos.append(d)
    return  datos

# Programa principal
nums = leerdatos()
#nums = [9, 8, 7.5, 6, 9.5, 7, 10, 6, 7]
prom = promedio(nums)
mp = maypresprom(nums, prom)
print('\nResumen \n')
print(f'Lista de números: {nums} y son {len(nums)}')
print(f'El promedio : {prom}')
print(f'Mayores promedio : {mp} y son {len(mp)}')