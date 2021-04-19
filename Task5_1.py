"""
5. Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение. Если фирма отработала с прибылью,
вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и
определите прибыль фирмы в расчете на одного сотрудника.
"""

revenue = float(input("Please enter a revenue value... "))
costs = float(input("Please enter a cost value... "))

result = revenue - costs

if result > 0:
    print(f"Congratulations! Your company is profitable ({result}) !")
    print(f"The profitability of revenue is {result / revenue:.3f}")

    persons = int(input("How many employees work for your company?... "))
    print(f"Profit per employee is {result / persons:.3f}")

elif result < 0:
    print(f"Your company is operating at a loss ({-result}) !")

else:
    print(f"Zero is also a good result! But it is stable!")
