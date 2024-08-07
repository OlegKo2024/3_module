print('ПОЗИЦИОННЫЕ И ИМЕНОВАНЫЕ ПАРАМЕТРЫ')
def print_param(a, b, c):
    print(a, b, c)

print_param(2,3,4)

"""
сколько параметров функция принимает, столько должны и внести ни больше ни меньше
можно переназначать параметры, если необходимо
позиционные должны быть перед именованными
*, обозначаем, что все справа именованные
"""

def print_param(*,a, b, c):
    print(a, b, c)

print_param(a=2,b=3,c=4)

print('ВОЗМОЖНОСТЬ ЗАДАВАТЬ ПАРАМЕТРЫ ПО УМОЛЧАНИЮ')
def default_param(a=2, b=2):
    print(a + b)

default_param()                 # если параметры заданы по умолчанию, то можно вызывать функцию без значений
default_param(3, 4)       # но можно и изменить параметры по умолчанию

"""
Но ряд ограничений:
параметр позиционный идет первым, именованный-по умолчанию не может быть первым
по умолчанию указываем конечные параметры
"""
def default_param(a, b=2):
    print(a + b)

default_param(3)                 # тогда первый указываем и все ок
default_param(3, 4)        # и также можем доопределять и переопределять

def default_param(a, b=2, c=5):
    print(a + b - c)

default_param(10)                 # тогда первый указываем, все остальные идут по умолчанию
default_param(3, 4)         # и также можем доопределять и переопределять и использовать по умолчанию

print('ПАРАМЕТРЫ СОЗДАЮТСЯ ПРИ ОПРЕДЕЛЕНИИ ФУНКЦИИ, НЕ В МОМЕНТ ЕЕ ВЫЗОВА' )

def default_param(a, b=2, c=[]):
    c.append(a)
    print(c)

default_param(10)                 # [10] - при первом вызове добавлся
default_param(3, 4)         # [10, 3] - новый элемент добавляется при каждом вызове

print('ЕСЛИ НАМ НУЖНО СПИСОК ПЕРЕОПРЕДЕЛЯТЬ КАЖДЫЙ РАЗ ПРИ ЗАПУСКЕ ТО ПРИШЕМ:')

"""
Когда мы работаем с параметрами по умолчанию, в качестве этих параметров мы указываем неизменяемые объекты. 
Нужно помнить, что эти значения параметров создаются не в момент, когда мы вызываем функцию, а создаются при её определении. 
Если мы в качестве какого-то изменяемого параметра точнее в качестве параметра по умолчанию укажем, например, список, то есть изменяемый объект. 
Этот список был создан в момент определения функции, и каждый вызов просто добавляем, в уже существующий список, новый элемент.
"""
def default_param(a, b=2, c=None):
    if c is None:
        c = []
        c.append(a)
    print(c)

default_param(10)                 # [10] - при первом вызове добавлся первый
default_param(3, 4)         # [3] - первый элемент добавляется при каж дополнительном вызове

"""
функция имеет возможность принимать параметры по умолчанию, что позволяет нам в момент вызова не передавать никаких аргументов. 
Но, если мы работаем с параметрами по умолчанию, мы их задаём либо конечным элементам, либо уж всем, которые присутствуют у нас в функции. 
И в качестве этих самых значений по умолчанию мы используем неизменяемые объекты.
"""