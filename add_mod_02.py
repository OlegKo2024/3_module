"""
ля решения задачи необходимо выполнить следующие действия:

1. Организовать цикл for, который проходит по всем числам от 3 до 20. Переменную цикла назовём условно k.

2. Внутри цикла for создать переменную, содержащую пустую строку. По условию задачи нам нужно будет выводить пары чисел в слитном написании, это делается как раз с помощью строк.

3. Организовать вложенные циклы for, которые проходят по всем числам от 1 до k и от i + 1 до k соответственно. Переменные циклов назовём условно i и j.

4. Проверить, делится ли k на сумму i и j без остатка. Если да, добавляет значения i и j в ранее объявленную строковую переменную.

5. После каждого прохода по внутренним циклам печатаем текущее значение k и строку string.
"""
print('Генератор пароля для числа')

number = int(input('Введите число от 3 до 20: '))
password = ''
for i in range(1, number):
    for j in range(i, number):
        if number % (i + j) == 0 and i != j:
            password += (f'{i}{j}')
print(f'{number} - {password}')


print('Генератор паролей для всех чисел интервала - FOR')

for k in range(3, 21):
    password = ''
    for i in range(1, k):
        for j in range(i, k):
            if k % (i + j) == 0 and i != j:
                password += f'{i}{j}'
    print(f'{k} - {password}')

print('Генератор паролей для всех чисел интервала - WHILE')

k = 3
while k <= 20:
    password = ''
    for i in range(1, k):
        for j in range(i, k):
            if k % (i + j) == 0 and i != j:
                password += f'{i}{j}'
    print(f'{k} - {password}')
    k += 1

print('Генератор с функциями')


def lock(start, end):
    for k in range(start, end):
        key(k)


def key(k):
    password = ''
    for i in range(1, k):
        for j in range(i, k):
            if k % (i + j) == 0 and i != j:
                password += f'{i}{j}'
    print(f'{k} - {password}')


lock(3, 21)
