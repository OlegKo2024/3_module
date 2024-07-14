def get_multiplied_digits(number):           # Напишите функцию get_multiplied_digits и параметр number в ней
    str_number = str(number)                 # Создайте переменную str_number и запишите строковое представление(str) числа number в неё
    first = int(str_number[0])               # Cоздайте переменную first и запишите в неё первый символ из str_number в числовом представлении(int)
    if len(str_number) > 1:                  # Когда длина str_number больше 1, возвращайте значение first * get_multiplied_digits(int(str_number[1:]))
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first                        # Если же длина str_number не больше 1, тогда вернуть оставшуюся цифру first

result = get_multiplied_digits(40203)
print(result)
