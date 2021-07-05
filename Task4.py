# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

pos = abs(int(input("Please enter a positive integer...")))

max = pos % 10

while pos >= 1:
    pos = pos // 10

    if pos % 10 > max:
        max = pos % 10

    if pos > 9:
        continue
    else:
        print("Maximum digit in a number = ", max)
        break
