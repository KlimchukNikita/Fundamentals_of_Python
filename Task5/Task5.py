# 5. Создать (программно) текстовый файл,
# записать в него программно набор чисел,
# разделенных пробелами.
# Программа должна подсчитывать сумму
# чисел в файле и выводить ее на экран.

def sum_of_numbers():
    try:
        with open('some_text.txt', 'w+') as some_text:
            numbers = input('Enter a set of numbers separated by a space...\n')

            some_text.writelines(numbers)
            number = numbers.split()

            print(sum(map(int, number)))

    except ValueError:
        print('Enter the set of numbers!')

sum_of_numbers()
