# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму
# этих чисел к полученной ранее сумме и после этого завершить программу.

def some_function ():

    sum_result = 0

    flag = False

    while flag == False:
        number = input('Enter numbers or Z to exit...').split()

        result = 0

        for element in range(len(number)):

            if number[element] == 'z' or number[element] == 'Z':
                flag = True
                break

            else:
                result = result + int(number[element])

        sum_result = sum_result + result

        print(f'Current sum = {sum_result}')

    print(f'Final sum = {sum_result}')

some_function()
