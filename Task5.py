# 5. Реализовать формирование списка,
# используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
#
# Подсказка: использовать функцию reduce().

from functools import reduce

some_list = [element for element in range(100, 1001) if element % 2 == 0]

def some_function(previous_element, element):
    return previous_element * element

print(reduce(some_function, some_list))
