# 7. Создать (не программно) текстовый файл, в котором каждая строка должна
# содержать данные о фирме: название, форма собственности, выручка, издержки.
#
# Пример строки файла: firm_1 ООО 10000 5000.
#
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
# а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
#
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки,
# также добавить ее в словарь (со значением убытков).
#
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта: [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.

import json

company_profit = {}
profit = {}

ordinary_profit = 0
average_profit = 0

i = 0

with open('some_text.txt', 'r') as some_text:
    for string in some_text:
        company_name, ownership_type, firm_revenue, company_costs = string.split()
        company_profit[company_name] = int(firm_revenue) - int(company_costs)

        if company_profit.setdefault(company_name) >= 0:
            ordinary_profit = ordinary_profit + company_profit.setdefault(company_name)
            i += 1

    if i != 0:
        average_profit = ordinary_profit / i
        print(f'Average profit = {average_profit:.2f}')

    else:
        print(f'There is no average profit. Work is at a loss!')

    profit = {'Average profit = ': round(average_profit)}
    company_profit.update(profit)
    print(f'The profit of each company = {company_profit}')

with open('some_json.json', 'w') as some_json:
    json.dump(company_profit, some_json)

    some_string = json.dumps(company_profit)
    print(f'A json file has been created with the following content... \n'f' {some_string}')
