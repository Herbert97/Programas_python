# Procesar pizza
ingr = {'T':1.50, 'P':3.50, 'C':3.74, 'A':0.40}
base = 15
st = 0
tot = 0
pedido = input('Ingredientes de tu pizza ? ').upper()

for i in pedido:
    if i in 'TPCA':
        st = st + ingr[i]

st = st + base

if st >=20 :
    tot = st - (st * 0.05)

print(f'El subtotal es : {st}')
print(f'El total es : {tot}') 