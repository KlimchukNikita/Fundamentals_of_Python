# 6. Реализовать структуру данных «Товары».
# Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и
# словарь с параметрами (характеристиками товара:
# название, цена, количество, единица измерения).
# Структуру нужно сформировать программно,
# т.е. запрашивать все данные у пользователя.
#
# Необходимо собрать аналитику о товарах.
# Реализовать словарь, в котором каждый ключ —
# характеристика товара, например название,
# а значение — список значений-характеристик,
# например список названий товаров.

products = []

characteristics = {'Name': '', 'Price': '', 'Quantity': '', 'Unit': ''}

information = {'Name': [], 'Price': [], 'Quantity': [], 'Unit': []}

number = 0

while True:
    interface = input("To exit the program, enter 'A'. Press 'Enter' to continue the program. To process the data enter 'B'").upper()

    if interface == 'A':
        break
    number += 1

    if interface == 'B':
        print('Current data...')

        for key, value in information.items():
            print(f'{key}:{value}')

    for product in characteristics.keys():
        feature = input(f'Enter characteristics "{product}"...')
        characteristics[product] = int(feature) if (product == 'Price' or product == 'Quantity') else feature
        information[product].append(characteristics[product])
        products.append((number, characteristics))

products = int(input("Enter the number of products..."))

number = 1

some_dict = []
some_list = []
some_info = {}

while number <= products:
    some_dict = dict({'Name': input("Enter the name..."), 'Price': input("Enter the price..."),
                    'Quantity': input('Enter the quantity...'), 'Unit': input("Enter the unit...")})

    some_list.append((number, some_dict))
    number += 1

    some_info = dict({'Name': some_dict.get('Name'), 'Price': some_dict.get('Price'),
                    'Quantity': some_dict.get('Quantity'),'Unit': some_dict.get('Unit')})

print(some_list)
print(some_info)
