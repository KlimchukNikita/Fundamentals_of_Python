"""
6. Спортсмен занимается ежедневными пробежками.
В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
Требуется определить номер дня, на который общий результат спортсмена составит
не менее b километров. Программа должна принимать значения параметров a и b и
выводить одно натуральное число — номер дня.
"""


def km(res_min, res_max, days):  # Let's use recursion!
    if res_min > res_max:
        return days

    else:
        return km(res_min * 1.1, res_max, days + 1)


print(km(int(input("Please enter an initial result... ")), int(input("Please enter the final result... ")), int()))
