# Mayor y menor de una lista de numeros
def mayor(lista):
    m = lista[0]
    for n in range(len(lista)):
        if lista[n] > m :
            m = lista[n]
    return m

def menor(lista):
    m = lista[0]
    for n in range(len(lista)):
        if lista[n] < m :
            m = lista[n]
    return m

def leerdatos():
    datos=[]
    while True:
        d=int(input("número: "))
        if d==-1:
            break
        datos.append(d)
    return datos

# Programa principal
nums = leerdatos()
#nums = [9, 8, 7.5, 6, 9.5, 7, 10, 6, 7]
print(f'Lista de números: {nums}')
may = mayor(nums)
men = menor(nums)
print('Resumen estadistico: \n')
print(f'Total numeros : {len(nums)}')
print(f'El menor : {men}')
print(f'El mayor : {may}')