# Temperaturas
def centimetros(inch):
    return ( inch* 2.54  )
def pies(mts):
    return ( mts*3.281 ) 


print('[ 1 ] Convertir pulgadas a centimetros')
print('[ 2 ] Convertir metros a pies')
op = int(input("Elige ? "))
if op==1 :
    inch = int(input('Dame una cantidad de pulgadas '))
    print(f'los centimetros son:  {centimetros(inch)}inch')
elif op==2:
    mts = int(input('Dame una cantidad de metros '))
    print(f'Los pies son:  {pies(mts)}ft')