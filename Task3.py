# 3. Создайте собственный класс-исключение, который должен проверять содержимое
# списка на наличие только чисел. Проверить работу исключения на реальном примере.
# Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.
#
# Примечание: длина списка не фиксирована.
# Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта,
# введя, например, команду “stop”. При этом скрипт завершается,
# сформированный список выводится на экран.
#
# Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
# При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента
# и вносить его в список, только если введено число. Класс-исключение должен не позволить
# пользователю ввести текст (не число) и отобразить соответствующее сообщение.
# При этом работа скрипта не должна завершаться.

class Some_Exception:

    def __init__(self, *args):
        self.some_list = []

    def some_input(self):

        while True:

            try:
                value = int(input('Enter values...'))
                self.some_list.append(value)
                print(f'Your current list... {self.some_list} \n ')

            except:
                print(f'Invalid value!')
                answer = input(f'To try one more time? Y / N ... ')

                if answer == 'Y' or answer == 'y':
                    print(try_except.some_input())

                elif answer == 'N' or answer == 'n':
                    return f'Exit the application'

                else:
                    return f'Exit the application'

try_except = Some_Exception(1)

print(try_except.some_input())