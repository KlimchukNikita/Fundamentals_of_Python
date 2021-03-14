# 2. Создать текстовый файл (не программно),
# сохранить в нем несколько строк,
# выполнить подсчет количества строк,
# количества слов в каждой строке.

some_file = open('some_text.txt', 'r')
some_text = some_file.read()
print(f'The content of this file... \n{some_text}')

some_file = open('some_text.txt', 'r')
some_text = some_file.readlines()
print(f'The number of lines in this file = {len(some_text)}')

some_file = open('some_text.txt', 'r')
some_text = some_file.readlines()
for i in range(len(some_text)):
    print(f'The number of characters in this file in the {i + 1} line {len(some_text[i])}')

some_file = open('some_text.txt', 'r')
some_text = some_file.read()
some_text = some_text.split()
print(f'Total word count = {len(some_text)}')

some_file.close()
