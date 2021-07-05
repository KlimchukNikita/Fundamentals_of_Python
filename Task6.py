# 6. Реализовать два небольших скрипта:
# а). Итератор, генерирующий целые числа, начиная с указанного,
# б). Итератор, повторяющий элементы некоторого списка, определенного заранее.
#
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Необходимо предусмотреть условие его завершения.
#
# Например, в первом задании выводим целые числа, начиная с 3,
# а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие,
# при котором повторение элементов списка будет прекращено.

from itertools import count
from itertools import cycle

def some_count_function(start_number, stop_number):
    for element in count(start_number):
        if element > stop_number:
            break
        else:
            print(element)

def some_cycle_function(some_list, iteration_1):
    i = 0
    iteration_2 = cycle(some_list)

    while i < iteration_1:
        print(next(iteration_2))
        i += 1

some_count_function(start_number = int(input("Enter start number... ")),
    stop_number = int(input("Enter stop number... ")))

some_cycle_function(some_list = [1, 2], iteration_1 = int(input("Enter iteration... ")))
