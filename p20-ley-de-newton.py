# calcula la segunda ley de newton donde (f=m*a)

print('Calculando  la segunda ley de newton')
print('calcular la fuerza.....[f]')
print('calcular la masa......[m]')
print('calcular la aceleracion....[a]')
op = str.lower(input('Elige una opcion ? '))
if op=='f':
    print('\ncalculando la fuerza ..')
    m = int(input('dame la masa? '))
    a = int(input('dame la aceleración? '))
    f = m * a
    print(f'la fuerza es {f}')
elif op=='m':
    print('\ncalculando la masa ..')
    f = int(input('dame la fuerza? '))
    a = int(input('dame la aceleración? '))
    m = f / a
    print(f'la masa es {m}')
elif op=='a':
    print('\ncalculando la aceleración ..')
    f = int(input('dame la fuerza? '))
    m = int(input('dame la masa? '))
    a = f / m
    print(f'la aceleración es {a}')
else :
    print('Opcion invalida !!')
print('\n Programa terminado, muchas gracias...')