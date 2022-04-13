# Comprension de listas
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(f'todos los números : {nums}')

pares = [ n for n in nums if n%2==0]
print(f'pares : {pares}')

impares = [ n for n in nums if n%2!=0]
print(f'impares : {impares}')

cuadrado = [ n**2 for n in nums ]
print(f'cuadrado : {cuadrado}')

cero = [n if n%5!=0 else 0 for n in nums]
print(f'cero si multiplo de 5 : {cero}')

de10 = [n for n in range(10,210,10)]
print(f'de 10 hasta el 100 : {de10}')