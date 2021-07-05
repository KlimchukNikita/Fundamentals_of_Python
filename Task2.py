# 2. Представлен список чисел.
# Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента.
#
# Подсказка: элементы, удовлетворяющие условию,
# оформить в виде списка. Для формирования списка использовать генератор.

some_list = [15, 2, 3, 1, 7, 5, 4, 10]

some_new_list = [element for number, element in enumerate(some_list)
    if some_list[number - 1] < some_list[number]]

print(f'Old list... {some_list}')
print(f'New list... {some_new_list}')
