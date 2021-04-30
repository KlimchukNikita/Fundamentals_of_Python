"""
4. Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""

num_user = int(input('Please enter a positive integer... '))
current_max = 0
num = num_user  # Variable to store the remainder

while num > 0:
    digit = num % 10  # Separating the last digit

    if digit > current_max:
        current_max = digit

        if current_max == 9:  # The maximum number is always 9
            break

    num = num // 10  # Separating the last digit

print(f'The largest digit in a number {num_user} =', current_max)
