# 4. Представлен список чисел.
# Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке.
# Для выполнения задания обязательно использовать генератор.

from itertools import permutations
from itertools import repeat
from itertools import combinations

some_list = [1, 2, 2, 3, 4, 1, 2]

some_new_list = [element for element in some_list if some_list.count(element) == 1]

print(some_new_list)
