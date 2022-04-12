# tabla de conversiones decimal,octal, binario
import os; os.system('clc')
inicio=int(input('numero de inicio: '))
fin=int(input('final de la tabla: '))
diferencia=fin-inicio
print(f"{'Tabla de conversiones ':^60}")
print('-'*70)
print('{p1:<15}{p2:^15}{p3:>10}{p4:>20}'.format(p1='Decimal',p2='Hexadecimal',p3='Octal',p4='Binario'))
print('-'*70)
for c in range(1,diferencia+1):
    inicio+=1
    print(f'\n:{inicio:d} :{"":<15}{inicio:x} : {"":<10}{inicio:o} : {"":<10} {inicio:b}')
print('-'*70)