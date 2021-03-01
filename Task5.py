# Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью,
# вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и
# определите прибыль фирмы в расчете на одного сотрудника.

profit = float(input("Enter company profit..."))
costs = float(input("Enter company costs..."))

if profit > costs:
    print(f"The company is working successfully. The profitability of revenue was {profit / costs:.2f}")
    workers = int(input("Enter the number of company employees..."))
    print(f"Profit per employee was {profit / workers:.2f}")

elif profit == costs:
    print("The company works at zero!")

else:
    print("The company is operating at a loss!")
