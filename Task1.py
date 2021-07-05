# 1. Реализовать функцию, принимающую два числа
# (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть
# обработку ситуации деления на ноль.

def some_function (dividend, divisor):
    try:
        quotient = dividend / divisor
        return quotient

    except ZeroDivisionError:
        return "Divisor cannot equal zero!"

    except ValueError:
        return "You must enter any number!"

print(some_function(int(input("Enter the dividend...")), int(input("Enter the divisor..."))))
