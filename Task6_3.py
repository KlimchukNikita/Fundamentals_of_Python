"""
6. Спортсмен занимается ежедневными пробежками.
В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
Требуется определить номер дня, на который общий результат спортсмена составит
не менее b километров. Программа должна принимать значения параметров a и b и
выводить одно натуральное число — номер дня.
"""

while 1:
    days = 1
    start_km = int(input('Please enter an initial result... '))
    last_km = int(input('Please enter the final result... '))

    if start_km > last_km:
        print('Invalid data entered!')

    else:
        while start_km < last_km:
            start_km += start_km * 0.1  # start_km = start_km + (start_km * 0.1)  # start_km *= 1.1
            days += 1  # days = days + 1

        print('The athlete will achieve the desired result in {} days!'.format(days))
        break
