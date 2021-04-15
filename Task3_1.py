"""
3. Узнайте у пользователя число n.
Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3.
Считаем 3 + 33 + 333 = 369.
"""

n = input("Please enter any positive number... ")

while int(n) < 0:
    print("This is a negative number!")
    n = input("Please enter any positive number... ")

print(f"{n} + {n + n} + {n + n + n} = {int(n) + int(n + n) + int(n + n + n)}")
