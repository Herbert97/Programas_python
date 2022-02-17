# verificar suma version 2
# 10 20 30      10 30 20    30 10 20    30 30 30    9 8 7
print('Verificar si la suma de 2 numeros es igual a un 3ero')
print('Dame 3 numeros enteros separados por espacio?')
n1, n2, n3 = input().split()
n1, n2, n3 = [int(n1), int(n2), int(n3)]
if n1 + n2 == n3:
    print('n1 + n2 = n3')
elif n1 + n3 == n2:
    print(f'n1 + n3 = n2')
elif n2 + n3 == n1:
    print(f'n2 + n3 = n1')
else:
    print('no hay sumas que coincidan')