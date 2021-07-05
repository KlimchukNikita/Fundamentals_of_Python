# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв
# и возвращающую его же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().

def int_func (word):
    print(word.title())

    return

int_func()

def some_function (word_1):
    splitting_word = word_1.split(' ')
    total = []

    for i in splitting_word:
        string_element = str(i)
        first_letter = string_element[:1].upper()
        word_2 = first_letter + string_element[1:]
        total.append(word_2)

    return total

print(some_function(int_func(input("Enter a word from lowercase letters..."))))
