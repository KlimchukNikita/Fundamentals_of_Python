# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

amount_of_elements = int(input("Enter the number of items in the list..."))

some_list = []

i = 0
element = 0

while i < amount_of_elements:
    some_list.append(input("Enter the next list item..."))
    i += 1

for elements in range(int(len(some_list)/2)):
    some_list[element], some_list[element + 1] = some_list [element + 1], some_list[element]
    element += 2

print(some_list)
