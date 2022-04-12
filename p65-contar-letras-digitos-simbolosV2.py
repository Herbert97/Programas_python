# contar letras, digitos, simbolos
frase = input('Dame una frase ? ')
car=dig=sim=0
car1=''
dig1=''
sim1=''
print(frase)
print(f'La frase tiene {len(frase)} caracteres')
for c in frase:
    if c.isalpha(): 
        car+=1 
        car1+=c
    elif c.isdigit(): 
        dig+=1 
        dig1+=c
    else: 
        sim+=1 
        sim1+=c
print(f'\nCaracteres {car}: {car1},\nDigitos {dig}: {dig1},\nSimbolos {sim}: {sim1}')