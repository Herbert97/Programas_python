# tabla de multiplicar con for

t = int(input('tabla ? '))
n = int(input('Limite ?'))
for r in range(1,n+1):
    print(f'{r} x {t} = {r*t}')