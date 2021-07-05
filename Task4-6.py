# 4. Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
#
# 5. Продолжить работу над первым заданием.
# Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное
# подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.
#
# 6. Продолжить работу над вторым заданием.
# Реализуйте механизм валидации вводимых пользователем данных. Например, для указания
# количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники»
# максимум возможностей, изученных на уроках по ООП.

class Storage:

    def __init__(self, name, price, quantity, number_of_sheets, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.number_of_sheets = number_of_sheets

        self.some_storage_full = []
        self.some_storage = []

        self.some_device = {'Device model': self.name,
                            'Price for one': self.price,
                            'Quantity': self.quantity}

    def __str__(self):
        return f'{self.name} price {self.price} quantity {self.quantity}'

    def reception(self):

        try:
            some_unit = input(f'Enter device model...')
            unit_price = int(input(f'Enter price for one...'))
            unit_quantity = int(input(f'Enter quantity...'))

            specifications = {'Device model': some_unit,
                              'Price for one': unit_price,
                              'Quantity': unit_quantity}

            self.some_device.update(specifications)
            self.some_storage.append(self.some_device)

            print(f'Current list...\n {self.some_storage}')

        except:
            return f'Input error!'

        print(f'Press "E" to exit... Press "Enter" to continue...')
        shutdown = input(f'Answer = ')

        if shutdown == 'E' or shutdown == 'e':
            self.some_storage_full.append(self.some_storage)

            print(f'Storage...\n {self.some_storage_full}')
            return f'Exit!'

        else:
            return Storage.reception(self)


class Printer(Storage):

    def to_print(self):
        return f'I print documents {self.numb} times!'


class Scanner(Storage):

    def to_scan(self):
        return f'I scan documents {self.numb} times!'


class Copier(Storage):

    def to_copy(self):
        return f'I copy documents {self.numb} times!'


first_device = Printer('Brother MFC-L2740DWR', 25000, 1000, 10000)
second_device = Scanner('Canon i-Sensys MF445dw', 35000, 100, 1000)
third_device = Copier('HP Color LaserJet Enterprise flow M880z', 715000, 10, 100)

print(first_device.reception())
print(second_device.reception())
print(third_device.reception())

print(first_device.to_print())
print(second_device.to_scan())
print(third_device.to_copy())
