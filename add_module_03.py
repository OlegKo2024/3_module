print('Вариант 1')
def sum_it_all(data_structure):
    total = 0
    if isinstance(data_structure, (list, tuple, set)):
        for i in data_structure:
            total += sum_it_all(i)
    elif isinstance(data_structure, dict):
        for key, value in data_structure.items():
            total += sum_it_all(key)
            total += sum_it_all(value)
    elif isinstance(data_structure, str):
        total += len(data_structure)
    elif isinstance(data_structure, (int, float)):
        total += data_structure
    return(total)

data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = sum_it_all(data_structure)
print(result)

print(len(data_structure))

print('Вариант 2')

total = 0
for i in data_structure:
    if type(i) == str:
        total += len(i)
    elif type(i) == list or type(i) == tuple or type(i) == set:
        for m in i:
            if type(m) == int or type(m) == float:
                total += m
            elif type(m) == str:
                total += len(m)
            elif type(m) == dict:
                for n in list(m.items()):
                    for o in n:
                        if type(o) == int:
                            total += o
                        elif type(o) == str:
                            total += len(o)
            elif type(m) == list or type(m) == tuple or type(m) == set:
                for p in m:
                    if p == ():
                        continue
                    elif type(p) == list or type(p) == tuple or type(p) == set:
                        for q in p:
                            if type(q) == list or type(q) == tuple or type(q) == set:
                                for r in q:
                                    if type(r) == int or type(r) == float:
                                        total += r
                                    elif type(r) == str:
                                        total += len(r)
                                    elif type(r) == list or type(r) == tuple or type(r) == set:
                                        for s in r:
                                            if type(s) == int or type(s) == float:
                                                total += s
                                            elif type(s) == str:
                                                total += len(s)
    elif type(i) == dict:
        for k in list(i.items()):
            for l in k:
                if type(l) == int:
                    total += l
                elif type(l) == str:
                    total += len(l)

print(total)
