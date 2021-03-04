# 5. Реализовать структуру «Рейтинг», представляющую собой невозрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

some_list = [9, 4, 7, 1, 8, 3, 6, 2, 5]

print(f"Rating - {some_list}")

number = int(input("Enter the number (If the entered number = 10, then the exit)..."))

while number != 10:
    for elements in range(len(some_list)):
        if some_list[elements] == number:
            some_list.insert(elements + 1, number)
            break

        elif some_list[0] < number:
            some_list.insert(0, number)

        elif some_list[-1] > number:
            some_list.append(number)

        elif some_list[elements] > number and some_list[elements + 1] < number:
            some_list.insert(elements + 1, number)

    print(f"Current rating - {some_list}")

    number = int(input("Enter the number (If the entered number = 10, then the exit)..."))

print("The number you entered = 10, exit!")
