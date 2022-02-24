# suma de pares e impares hasta donde el usuario decida
n = int(input("Hasta donde deseas los numeros? "))
s = 0
print("\nNumeros impares:")
for i in range(1,n+1,2):
    s += i
    print(i,end=" ")
print(f'\nSuma impares: {s}')

s = 0
print("\nNumeros pares:")
for i in range(2,n+1,2):
    s += i
    print(i,end=" ")
print(f'\nSuma pares: {s}')