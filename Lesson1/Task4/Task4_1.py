"""
4. Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""

num_init = int(input('Please enter a positive integer... '))
maximum = num_init % 10
num = num_init

while num > 0:
    digit = num % 10

    if digit > maximum:
        maximum = digit

        if digit == 9:
            break

    num = num // 10
    print(num)

print(f"The largest digit in a number {num_init} is {maximum}")
