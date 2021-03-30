# 7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения
# и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры
# класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class Complex_number:

    def __init__(self, a, b, *args):
        self.a = a
        self.b = b

        self.z = 'a + b * i'

    def __add__(self, other):
        print(f'The sum of two complex numbers...')
        return f'z = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'The multiplication of two complex numbers...')
        return f'z = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'z = {self.a} + {self.b} * i'


first_number = Complex_number(1, -2)
second_number = Complex_number(3, 4)

print(first_number)
print(second_number)

print(first_number + second_number)
print(first_number * second_number)
