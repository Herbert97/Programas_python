# Suma números en un rango

def suma_rango(ini, fin, caracter):
    s = 0
    if caracter=='P':
        for i in range(ini, fin+1,2):
            if i%2==0:
                s += i       
    if caracter=='I':
        for i in range(ini, fin+1,1):
            if i%2 !=0:
                s+=i
    return s   

print('dame un rango de valores a sumar')
ini=int(input('dame el inicio: '))
fin=int(input('dame el fin?: '))
caracter=(input('pares o impares P o I?: '))
print(f'la suma del rango es: {suma_rango(ini,fin,caracter)}')
