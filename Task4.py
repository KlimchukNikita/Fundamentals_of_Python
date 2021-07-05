# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если слово длинное, выводить только первые 10 букв в слове.

some_string = input("Enter the string...")

some_words = []

number = 1

for elements in range(some_string.count(' ') + 1):
    some_words = some_string.split()

    if len(str(some_words)) <= 10:
        print(f" {number} {some_words [elements]}")
        number += 1

    else:
        print(f" {number} {some_words [elements] [0:10]}")
        number += 1
