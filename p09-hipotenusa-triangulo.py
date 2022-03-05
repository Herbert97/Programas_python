# programa para calcular la hipotenusa de un triangulo rectangulo.
import math

print('calculando la hipotenusa de un triangulo')
lado1=int(input('dame el primer lado del triangulo '))
lado2=int(input('dame el segundo lado del triangulo'))
hipo=(lado1*lado1+lado2*lado2)
hipotenusa=math.sqrt(hipo)
print(f'suma y potenciacion de lado 1 y lado 2 {hipo}')
print(f'Hipotenusa del triangulo rectangulo {hipotenusa}')