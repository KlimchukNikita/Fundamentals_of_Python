# 1. Реализовать класс «Дата», функция-конструктор которого должна
# принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год
# и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Data:

    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        some_date = []

        for i in day_month_year.split():
            if i != '-': some_date.append(i)

        return int(some_date[0]), int(some_date[1]), int(some_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2021 >= year >= 0:
                    return f'All right!'

                else:
                    return f'Invalid year!'

            else:
                return f'Invalid month!'

        else:
            return f'Invalid day!'

    def __str__(self):
        return f'The current date {Data.extract(self.day_month_year)}'

today = Data('25 - 12 - 1999')

print(today)

print(Data.valid(10, 10, 2022))
print(today.valid(15, 15, 2011))

print(Data.extract('25 - 02 - 2010'))
print(today.extract('30 - 03 - 2020'))
