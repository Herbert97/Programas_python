# factorial
n = int(input("De que numero deseas factorial? "))
f = 1
for i in range(1,n+1):
    f *=  i
print(f"El factorial es: {f}")