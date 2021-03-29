# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно
# обработать эту ситуацию и не завершиться с ошибкой.

class Dangerous_Division:

    def __init__(self, dividend, divisor):
        self.dividend = dividend
        self.divisor = divisor

    @staticmethod
    def division_operation(dividend, divisor):

        try:
            return (dividend / divisor)

        except:
            return (f'Division by zero is not allowed!')

div = Dangerous_Division(100, 100)

print(Dangerous_Division.division_operation(100, 0))
print(Dangerous_Division.division_operation(100, 0.01))

print(div.division_operation(100, 0))
print(div.division_operation(100, 0.01))
