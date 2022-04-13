# Iterar sobre los elementos de la lista
nums = [2, 4, 6, 8, 10, 12, 14, 16]
print(f'todos los números : {nums}')

print('\nIterar con ciclo for : ', end='')
for n in nums:
    print(n,end=' ')  

print('\nIterar con ciclo range : ', end='')
for i in range(len(nums)):
    print(nums[i], end=' ')

print('\nIterar con ciclo while : ', end='')
i=0
while i<len(nums):
    print(nums[i], end=' ')
    i+=1
    
print(f'\nIterar con comprension : ', end='')
[print(n, end=' ') for n in nums]