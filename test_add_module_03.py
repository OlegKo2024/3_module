print('Задание "Раз, два, три, четыре, пять .... Это не всё?":')
print('Вариант 1')
def sum_it_all(data_structure):
    total = 0
    if isinstance(data_structure, str):
        for i in data_structure:
            total += 1
    if isinstance(data_structure, (int, float)):
        total += data_structure
    if isinstance(data_structure, (list, tuple, set)):
        for i in data_structure:
            total += sum_it_all(i)
    if isinstance(data_structure, dict):
        for key, value in data_structure.items():
            total += sum_it_all(key)
            total += sum_it_all(value)
    return total

data_structure = [[1, 2, 3],{'a': 4, 'b': 5},(6, {'cube': 7, 'drum': 8}),"Hello",((), [{(2, 'Urban', ('Urban2', 35))}])]

result = sum_it_all(data_structure)
print(result)

print('One code')
total = 0
if isinstance(data_structure, (list, tuple, set, dict)):
    for i in data_structure:
        total += sum_it_all(i)
print(total)

print('Workings')
data_str = "Oleg Nikita"
data_int_float = 4.6
data_list = [4.4, 5.6, 7]
data_list_add = ['Oleg', True, 100]
data_tuple = (4.4, 5.6, 7)
data_tuple_add = ('Oleg', True, 100)
data_dict = {'Name': 'Oleg', 'Age': 57}
data_dict_add = {'Name': 'Tania', 'Age': 55, 'Children': 2}

print('Count str')
print(isinstance(data_str, str))                # True
if isinstance(data_str, str):
    print(data_str.count(''))                   # 12

print('FOR str')
count = 0
if isinstance(data_str, str):
    for i in data_str:
        count += 1
print(count)                                    # 11

print('Simple int')
total = 0
if isinstance(data_int_float, (int, float)):
    total += round(data_int_float)
print(total)

print('Sum list')
if isinstance(data_list, list):
    total = int(sum(data_list))
print(total)                        # 17

print('For list_num_00')
total = 0
if isinstance(data_list, list):
    for i in data_list:
        total += i
print(total)                        # 17

print('For list_num_01')
total = 0
if isinstance(data_list, list):
    for i in range(len(data_list)):
        total += data_list[i]
print(total)                        # 17

print('For list_all')
total = 0
if isinstance(data_list, list) and isinstance(data_list_add, list):
    data_list_all = data_list + data_list_add
    for i in range(len(data_list_all)):
        if type(data_list_all[i]) == int or type(data_list_all[i]) == float:
            total += data_list_all[i]
print(data_list_all)                                # [4.4, 5.6, 7, 'Oleg', True, 100]
print(len(data_list_all))                           # 6
print(total)                                        # 117

print('Sum tuple')
if isinstance(data_tuple, tuple):
    total = int(sum(data_tuple))
print(total)                        # 17

print('For tuple')
total = 0
if isinstance(data_tuple, tuple):
    for i in data_tuple:
        total += i
print(total)

print('For tuple')
total = 0
if isinstance(data_tuple, tuple) and isinstance(data_tuple_add, tuple):
    data_tuple_all = data_tuple + data_tuple_add
    for i in range(len(data_tuple_all)):
        if type(data_tuple_all[i]) == int or type(data_tuple_all[i]) == float:
            total += data_tuple_all[i]
print(data_tuple_all)                                # [4.4, 5.6, 7, 'Oleg', True, 100]
print(len(data_tuple_all))                           # 6
print(total)

print('For dict')
print('https://realpython.com/python-dicts/')
total = 0
if isinstance(data_dict, dict) and isinstance(data_dict_add, dict):
    data_dict.update({'Children': 3})
    data_dict_updated = {**data_dict, **data_dict_add}
    data_dict_all = list(data_dict.items()) + list(data_dict_add.items())
    data_dict_all_ = [data_dict, data_dict_add]
    for i in data_dict_all_:
        for j in list(i.items()):
            for k in j:
                if type(k) == int:
                    total += k
                if type(k) == str:
                    total += len(k)

print(data_dict)
print(data_dict_updated)
print(data_dict_all)
print(data_dict_all_)
print(len(data_dict_all_))
print(total)



print('Вариант 2')
def sum_it_all(data_structure):
    summa = 0
    if isinstance(data_structure, dict):
        for key, value in data_structure.items():
            summa += sum_it_all(key)
            summa += sum_it_all(value)
    if isinstance(data_structure, (list, tuple, set)):
        for item in data_structure:
            summa += sum_it_all(item)
    if isinstance(data_structure, (int, float)):
        summa += data_structure
    if isinstance(data_structure, str):
        summa += len(data_structure)
    return summa


data_structure = [[1, 2, 3],{'a': 4, 'b': 5},(6, {'cube': 7, 'drum': 8}),"Hello",((), [{(2, 'Urban', ('Urban2', 35))}])]

result = sum_it_all(data_structure)
print(result)


# def sum_list(l):
#     if len(l) == 0:
#         return 0
#     return l[0] + sum_list(l[1:])
#
# print(sum_list([3, 4, 5, 6, 7]))



