"""
string = 'Nikita'
arr_message = []
arr_message = [arr_message.append(i) for i in string]
print(arr_message)

string = 'Nikita'
arr_message = []
arr_message = [arr_message.append(i) for i in string[0:]]
print(arr_message)

string = 'Tania'
arr_message = [i for i in string]
print(arr_message)

string = 'Oleg'
arr_message = []
for i in string:
    arr_message.append(i)
print(arr_message)
"""
# list_to_search = [i.upper() for i in list_to_search]
# student['Mark'] = [int(m) for m in arr[2:]]

# if arr_message_ is not '@':
# print(f"Невозможно отправить письмо с адреса <sender> на адрес <recipient>")

"""
def send_email(message, recipient, sender = 'university.help@gmail.com'):
    arr_message_ = []
    arr_message_ = [i.append(i) for i in message]
    if message is not '@':
        print(f"Невозможно отправить письмо с адреса <sender> на адрес <recipient>")

list_to_search = [i.upper() for i in list_to_search]

send_email('okok', 'nikita')
"""
# s = 'university.help@gmail.com'
# it_contains = False
# for i in s:
#     if i == '@':
#         it_contains = True
#         print('True')
#         break

print('YES')
s = 'vas@gmail.com'
r = 'uni@gmail.com'
it_contains = False
for i in r:
    if i == '@':
        it_contains = True
        for j in s:
            if j == '@':
                it_contains = True
                print('Письмо успешно отправлено с адреса', s, 'на адрес', r)
                break
        else:
            print('Невозможно отправить письмо с адреса', s, 'на адрес', r)

print('NO')
s = 'vasgmail.com'
r = 'uni@gmail.com'
it_contains = False
for i in r:
    if i == '@':
        it_contains = True
        for i in s:
            if i == '@':
                it_contains = True
                print('Письмо успешно отправлено с адреса', s, 'на адрес', r)
                break
        else:
            print('Невозможно отправить письмо с адреса', s, 'на адрес', r)

print('FUNCTION')
def send_email(message, recipient, sender='university.help@gmail.com'):
    it_contains = False
    for i in recipient:
        if i == '@':
            it_contains = True
            for i in sender:
                if i == '@':
                    it_contains = True
                    print('Письмо успешно отправлено с адреса', sender, 'на адрес', recipient)
                    break
            else:
                return 'Невозможно отправить письмо с адреса', sender, 'на адрес', recipient

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')

print('НЕ ПОЛУЧАЕТСЯ ПОЛУЧИТЬ ОТРИЦАТЕДЛЬНЫЙ ОТВЕТ, КОГДА НЕТ @')


"""
print('ИСПОЛЬЗУЯ ЛОГИЧЕСКИЕ ЗНАЧЕНИЯ В ФУНКЦИЯХ')
def contains(string, list_to_search):
    string = string.upper()
    list_to_search = [i.upper() for i in list_to_search]
    print(string)
    print(list_to_search)
    it_contains = True
    for i in list_to_search:
        if i != string:
            it_contains = False
            return 'False'
        else:
            return 'True'
"""