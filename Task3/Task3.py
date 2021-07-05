# 3. Создать текстовый файл (не программно),
# построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

with open('some_text.txt', 'r') as some_file:
    good_salary = []
    bad_salary = []

    some_list = some_file.read().split('\n')

    for i in some_list:
        i = i.split()

        if int(i[1]) < 20000:
            bad_salary.append(i[0])
            good_salary.append(i[1])

print(f'Salary less than 20,000... {bad_salary}, average salary... {sum(map(int, good_salary)) / len(good_salary)}')
