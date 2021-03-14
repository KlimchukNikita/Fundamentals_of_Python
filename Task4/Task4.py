# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл
# на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

some_dictionary = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
some_file = []

with open('some_text.txt', 'r') as some_text:

    for i in some_text:
        i = i.split(' ', 1)
        some_file.append(some_dictionary[i[0]] + ' ' + i[1])
    print(some_file)

with open('new_some_text.txt', 'w', encoding = 'UTF-8') as new_some_text:
    new_some_text.writelines(some_file)
