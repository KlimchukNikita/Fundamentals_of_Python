# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

some_list = [848, -273, 55.55, True, 'RSREU', None]

def some_type(some_element):
    for some_element in range(len(some_list)):
        print(type(some_list[some_element]))
    return

some_type(list)
