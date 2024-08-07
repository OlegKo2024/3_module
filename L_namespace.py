"""
Пространство имен – это своего рода система, которая отвечает за то, чтобы все имена в программе были уникальными и
могли использоваться без каких-либо проблем или конфликтов.
Глобальное пространство имен - переменные с которыми оперирует вся система
Локальное - те переменные, что я создал в рамках созданной мной функции
они работают/существуют только в пределах созданной нами функции
к глобальной переменной можно обратиться в функции
"""
a = 1
b = 5

def local():
    c = 10
    d = 20
    print(a, b, 'Global')
    print (c, d, 'Local')


local()
print(a, b)

# 1 5 Global
# 10 20 Local
"""
можно ее переназначить нов пределах функции
но зарамками функции они сохранят свои значения, как глобальные
"""
def local():
    a = 'Oleg'
    b = 1966
    c = 10
    d = 20
    print(a, b, 'Global')
    print (c, d, 'Local')


local()
print(a, b)
# Oleg 1966 Global
# 10 20 Local
# 1 5

"""
Но если нам необходимо взаимодействовать с переменными из глобального пространства внутри локального пространства имен 
функции, то надо прописать в самом начале функции, что используем глобальные переменные «a» и «b» - global a, b
"""
def local():
    global a, b
    a = 'Oleg'
    b = 1966
    c = 10
    d = 20
    print(a, b, 'Global')
    print (c, d, 'Local')


local()
print(a, b)
# Oleg 1966 Global
# 10 20 Local
# Oleg 1966
# таким образом во время вызова функции мы переопределили значения переменных «a» и «b» из глобального пространства имен

