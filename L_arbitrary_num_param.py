print('Произвольное число параметров')


def summator(*values):
    s = 0
    for i in values:
        s += i
    return s

s = summator(1, 2, 3)
print(s)

print('Можно комбинировать')

def summator(txt, *values):
    s = 0
    for i in values:
        s += i
    return f'{txt} {s}'

print(summator('Значение: ', 1, 2, 3))      # Значение:  6


print('Можно добавлять параметр по умолчанию')
def summator(txt, *values, type='sum'):
    s = 0
    for i in values:
        s += i
    return f'{txt} {s} {type}'

print(summator('Значение: ', 1, 2, 3))      # Значение:  6 sum

print('** - СЛОВАРИ')

def info(**values):
    print(type(values))
    print(values)
    for key, value in values.items():
        print(key, value)

info(name='Oleg', age='57')
# <class 'dict'>
# {'name': 'Oleg', 'age': '57'}
# name Oleg
# age 57

print('Переменное количество именованных параметров можем комбинировать с переменным количеством позиционных параметров')
'''
но позиционные параметры никогда не идут после именованных - # def info(**values, *args): - так нельзя!
'''

def info(*args, **values):
    print(type(args))
    print(type(values))
    print(args)
    print(values)
    for key, value in values.items():
        print(key, value)
    print(args)

info(5, 'love', name='Oleg', age='57')
# <class 'tuple'>
# <class 'dict'>
# (5, 'love') - кортеж
# {'name': 'Oleg', 'age': '57'} - словарь
# name Oleg
# age 57
# (5, 'love')

print('Объединили все виды параметров в одном - пример использования параметров всех типов')
def info(value, *args, names='Dan', **values): # позиционный, произвольное кол-во позиц. параметров, именованный параметр, произвольное кол-во именованных параметров
    print(type(args))
    print(type(values))
    print(args)
    print(values)
    for key, value in values.items():
        print(key, value)
    print(args)

info(5, 'love', name='Oleg', age='57')
# позиционный, произвольное кол-во позиционных параметров, именованный параметр, произвольное кол-во именованных параметров


print('Функция общая находит сумму чисел')

def sum_power(n, *args, txt='Сумма в степени'):
    s = 0
    for i in range(len(args)):
        s += args[i] ** n
    return f'{txt}: {s}'

print(sum_power(1, 1, 2, 3))
print(sum_power(2, 1, 2, 3))
# Сумма в степени: 6
# Сумма в степени: 14




