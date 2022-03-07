# suma de pares  hasta donde el usuario decida
n = int(input("Hasta donde deseas los numeros pares ? "))
s = 0
print("\nNumeros pares:")
for i in range(2,n+1,2):
    s += i
    print(i,end=" ")
print(f'\nSuma pares: {s}')