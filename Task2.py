# 2. Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать параметры
# как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

def some_function (name, surname, year, city, email, number):

    print(name, surname, year, city, email, number)

some_function(name = 'Nikita', surname = 'Klimchuk', year = 1999, city = 'Ryazan', email = 'KlimchukNik', number = 123456789)
