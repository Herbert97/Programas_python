# Remover elementos de la lista
nums = [1, 3, 5, 7, 9, 11, 99, 15, 88, 19, 100]
print(f'todos los números : {nums}')
nums.remove(99)
print(f'remover 99 : {nums}')
nums.pop(8)
print(f'remover [8] : {nums}')
nums.pop()
print(f'remover el ultimo: 100 : {nums}')
nums.clear()
print(f'remover todos : {nums}')