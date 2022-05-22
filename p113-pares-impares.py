# Pares e impares en una lista
import os

def pares_impares(nums):
    pares=[]
    impares=[]
    for n in nums:
        if n % 2 == 0 : pares.append(n)
        else: impares.append(n)
    return pares, impares

# Programa principal
nums = [9, 8, 7.5, 6, 9.5, 7, 10, 6, 7]
os.system('clear')
pares, impares = pares_impares(nums)
print(f'La numeros : {nums} -> {len(nums)}')
print(f'Los pares : {pares} -> {len(pares)}')
print(f'Los impares: {impares} -> {len(impares)}')