# 1. Поработайте с переменными,
# создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел
# и строк и сохраните в переменные,
# выведите на экран.

var1 = 100
var2 = 200

print("Variables var1 and var2 -", var1, var2)

str1 = input("Enter the first string...")
num1 = int(input("Enter the first number..."))

str2 = input("Enter the second string...")
num2 = int(input("Enter the second number..."))

print("All entered values - %10s %5d %10s %5d" % (str1, num1, str2, num2))
