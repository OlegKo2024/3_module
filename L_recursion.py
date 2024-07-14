
"""
Рекурсия — это такой способ определения функции или описание функции, когда эта самая функция вызывает саму себя.
Два правила:
- в какой момент остановиться
- в какой момент функция вызывает саму себя
Пример ниже:
- останавливаться, когда параметр n будет равен 0
- когда n не равен 0, будем возвращать этот самый параметр и при этом добавлять вызов функции,
но только с параметром, который меньше на единицу( n + summa(n-1))
"""
def sum(n):
    if n == 0:
        return 0
    else:
        return n + sum(n-1)

print(sum(5))                   # 15

print('LIFO')
stack = []
print(stack)
stack.append(1)
print(stack)
stack.append(2)
print(stack)
stack.append(3)
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)