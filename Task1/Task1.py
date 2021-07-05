# 1. Создать программно файл в текстовом формате,
# записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

some_file = open('some_text.txt', 'w')
some_text = input('Enter text... \n')

while some_text:
    some_file.writelines(some_text)
    some_text = input('Enter text... \n')

    if not some_text:
        break

some_file.close()

some_file = open('some_text.txt', 'r')
some_text = some_file.readlines()
print(some_text)

some_file.close()
