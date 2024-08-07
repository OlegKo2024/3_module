"""
Одна “звездочка” используется для распаковки и запаковки именно позиционных параметров, которые содержат один элемент:
списки, кортежи, множества и т.д.;
Две “звездочки” используются для запаковки и распаковки именованных параметров(рис.1). В Python такая коллекция одна -
словари. В них элементы хранятся парами.
"""
print('ARGS - ПОЗИЦИОННЫЕ ПАРАМЕТРЫ - СПИСКИ КОРТЕЖИ МНОЖЕСТВА')
print('УПАКОВКА')


def position_param(*args):
    print(args)


position_param(1, 2, 3, 4, 5)  # (1, 2, 3, 4, 5) получили кортеж

l = [2, 3, 4, 5]
position_param(l)  # ([2, 3, 4, 5],) получили кортеж за первым параметром

print('РАСПАКОВКА')


def position_param(*args):
    print(*args)


position_param(1, 2, 3, 4, 5)  # 1 2 3 4 5 - если поставим звездочку, то распакуем кортеж

l = [2, 3, 4, 5]
position_param(l)  # [2, 3, 4, 5] - кортежа нет, есть список, по сути его и вывели

"""
Одну “звездочку” мы можем поставить тогда, когда не уверены или не знаем сколько у нас будет параметров. Как правило, 
если функция принимает больше 7 параметров, используют оператор “*args”.
"""


def position_param(a, b, c):
    print(a, b, c)


l = [2, 3, 4]
position_param(l, 5, 6)  # [2, 3, 4] 5 6 - параметры списка встали на место первого параметра


def position_param(a, b, c):
    print(a, b, c)


l = [2, 3, 4]
position_param(*l)  # 2 3 4 - для того, чтобы параметры стали на свои места ставим *


def position_param(a, b, c):
    print(a, b, c)


l = [2, 3]
position_param(1, *l)  # 1 2 3 - если параметров в списке не хватает могу дополнить так как позиционные
position_param(c=5, *l)  # 2 3 5 - могу дополнить любым параметром


def position_param(*args):
    print(*args)


l = [2, 3, 4, 5]
position_param(*l)  # 2 3 4 5 - распаковал в том случае, если кол-во параметров не известно

print('KWARGS - ИМЕНОВАННЫЕ ПАРАМЕТРЫ -  СЛОВАРИ')


def position_param(a, b, c):
    print(a, b, c)


dict_ = {'a': 1, 'b': 2, 'c': 3}
position_param(**dict_)  # 1 2 3 - если хочу передать в функцию значения, то распаковываю и передаю

"""
!Заметьте, что ключи должны соответствовать названиям параметров функции, иначе выдаст ошибку. Если же вы не хотите 
придавать конкретики названиям ключей, то вместо a, b, c , мы можем написать “**kwargs”. 
Но когда явно указаны параметры, эти ключи должны соответствовать.
"""


def position_param(**kwargs):
    print(kwargs)


dict_ = {'a': 1, 'b': 2, 'c': 3}
position_param(**dict_)  # {'a': 1, 'b': 2, 'c': 3} - если не хотим привязку к параметрам функции

"""
Здесь же происходит то же самое, что происходило и при распаковке позиционных параметров, с помощью списка. 
Единственное отличие, что здесь у нас именованные параметры. Также “**kwargs” часто используется только после “*args”. 
Как правило, именованные параметры идут после позиционных.

Кроме того, раз у нас есть значение параметров, мы можем, например, с помощью цикла for вывести сами ключи(рис.9). 
Можно пройтись по ключам и значениям этих параметров, только используя метод items для словарей, и вывести ключ и значение
"""
print('KWARGS - РАСПАКОВКА С ПОМОЩЬЮ FOR')


def position_param(**kwargs):
    for key in kwargs:
        print(key)


dict_ = {'a': 1, 'b': 2, 'c': 3}
position_param(**dict_)


# a
# b
# c

def position_param(**kwargs):
    for key, value in kwargs.items():
        print(key, value)


dict_ = {'a': 1, 'b': 2, 'c': 3}
position_param(**dict_)
# a 1
# b 2
# c 3

print('РАСПАКОВКА С ПОМОЩЬЮ СПИСКА И СЛОВАРЯ')


def position_param(a, b, c):
    print(a, b, c)


l = [2, 4]
dict_ = {'c': 1}
position_param(*l, **dict_)  # 2 4 1 - нельзя именованые ставить перед позиционными
