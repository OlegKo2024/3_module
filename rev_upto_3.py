print('if elif else')
"""
name = input('Enter: ')
if name == 'Oleg':
    print('I know you')
print('Hi', name)

name = input('Enter: ')
if name == 'Oleg':
    print('I know you')
else:
    print('Hi', name)
"""
print('According to the UN Convention of the Rights of the Child')
"""
ADULT_AGE = 18
def analyze_age(age):
   if age < ADULT_AGE and age > 0:
       print("You are a child")
   elif age >= ADULT_AGE:         # если оставить if, то компьютер воспринимает это как еще один блок условий и после него включает else
       print("You are an adult")
   else:
       print("The age must be a positive integer!")

print(analyze_age(16))
# если if: You are a child
# The age must be a positive integer!
# если eif: You are a child
# Когда мы используем команду if, мы создаем блок условий.
# То есть у нас здесь первый блок условий, 2 блок условий, 3 блока условий.
# С командой if наш блок условий начинается. Однако здесь нужно сделать так, чтобы
# при выполнении одного условия компьютер дальше не проверял другие условия.
# Чтобы сделать так, нужно дополнить этот блок условий командами elif.
"""

print('Стиль кода')
# import this
print('41 вопрос о работе со строками в Python')
# https://habr.com/ru/companies/ruvds/articles/500296/

print('Лотерея')

import random
def lottery(*args):
    # print(args)
    args = list(args)
    # print(args)
    top_prioriry = random.choice(args)
    args.remove(top_prioriry)
    second_choice = random.choice(args)
    return top_prioriry, second_choice

top_priority, second_choice = lottery('Bonn', 'Munich', 'Aahen', 'Karlsruhe')
print(top_priority, second_choice)
