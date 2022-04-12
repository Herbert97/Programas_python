# contar vocales y consonantes
frase = input('Dame una frase ? ')
voc=cons=0
voc1=''
con1=''
frase.lower()
print(frase)
print(f'La frase tiene {len(frase)} caracteres')
for c in frase:
    if c.isalpha():
        if c in 'aeiou':
            voc += 1
            voc1+=c
        else:
            cons += 1
            con1 +=c
print(f'Vocales = {voc} estas son las vocales : {voc1}')
print(f'Consonantes = {cons} estas son las consonantes: {con1}')