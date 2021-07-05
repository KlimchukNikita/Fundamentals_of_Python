# 3. Реализовать функцию my_func(), которая
# принимает три позиционных аргумента, и
# возвращает сумму наибольших двух аргументов.

def some_function(argument_1 , argument_2, argument_3):

    if argument_1 >= argument_3 and argument_2 >= argument_3:
        return argument_1 + argument_2

    elif argument_1 > argument_2 and argument_1 < argument_3:
        return argument_1 + argument_3

    else:
        return argument_2 + argument_3

print(some_function(int(input("Enter the first argument...")), int(input("Enter the second argument...")), int(input("Enter the third argument..."))))
