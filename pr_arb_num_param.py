def single_root_words(root_word, *other_words):
    same_words = []                                 # Создать пустой список same_words
    root_word = root_word.lower()                   # Привести к единому формату
    other_words = [i.lower() for i in other_words]  # Привести к единому формату
    for i in range(len(other_words)):               # Перебрать список по количеству элементов
        if root_word in other_words[i]:             # Задать условие наличия корня в списке
            same_words.append(other_words[i])       # Если найдено, добавить в список
        elif other_words[i] in root_word:           # Задать условие наличия корня из списка в позиционной переменной
            same_words.append(other_words[i])       # Если найдено, добавить в список
    return same_words                               # Сформировать список


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')  # передать параметры
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')     # передать параметры
print(result1)                                      # Вывести на консоль результат1
print(result2)                                      # Вывести на консоль результат2

