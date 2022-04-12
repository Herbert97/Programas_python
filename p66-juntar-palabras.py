#juntar palabras concatenacion de las palabras separadas por letras.

print('las palabras se juntaran intercalando las letras, ambas palabras deben tener la misma longitud')

palabra1=input('dame una palabra: ')
palabra2=input('dame la segunda palabra: ')

cuenta1=len(palabra1)
cuenta2=len(palabra2)
frase=''
if cuenta1 ==cuenta2:
    for c  in palabra1:
        for d in palabra2:
            frase=frase+c+d               
else:
    print('las frases no son de la misma logitud')
print(f'las palabras juntas son: {frase}')
