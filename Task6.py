# 6. Спортсмен занимается ежедневными пробежками.
# В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена составит
# не менее b километров. Программа должна принимать значения параметров a и b и
# выводить одно натуральное число — номер дня.

a = int(input("Enter your first day run results in km..."))
b = int(input("Enter the total desired result in km..."))

result_days = 1
result_km = a

while result_km < b:
    a = a + 0.1 * a
    result_days += 1
    result_km = result_km + a

print(f"You will reach the required indicators for the %.d day" % result_days)
