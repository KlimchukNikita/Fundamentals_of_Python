"""
6. Спортсмен занимается ежедневными пробежками.
В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
Требуется определить номер дня, на который общий результат спортсмена составит
не менее b километров. Программа должна принимать значения параметров a и b и
выводить одно натуральное число — номер дня.
"""

while True:
    days = 1
    start_km = float(input("Please enter an initial result... "))
    final_km = float(input("Please enter the final result... "))

    if start_km <= 0 or final_km < 0:
        print("Results must be greater than zero! Start value != 0")

    else:
        while start_km < final_km:
            start_km *= 1.1
            days += 1
        print(f"The athlete will achieve the desired result in {days} days!")
