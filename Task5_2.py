"""
5. Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение. Если фирма отработала с прибылью,
вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и
определите прибыль фирмы в расчете на одного сотрудника.
"""

revenue = float(input('Please enter a revenue value... '))
costs = float(input('Please enter a cost value... '))

result = revenue - costs

if result > 0:
    print('The company works with a profit equal to', result)
    print('The profitability is', result / revenue)

    people = int(input('Please enter the number of employees... '))
    print(f'Profit per employee is {result / people:.2f}')

elif result < 0:
    print('Your company is operating at a loss equal to', result)

else:
    print('Your company is wasted!')
