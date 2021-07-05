# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
#
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
# Проверить работу этих методов на реальных данных.
#
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property.

class Clothes:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_coat_pattern(self):
        return self.width / 6.5 + 0.5

    def get_suit_pattern(self):
        return self.height * 2 + 0.3

    @property
    def get_total_expense(self):
        return str(f'Total fabric consumption = {(self.width / 6.5 + 0.5) + (self.height * 2 + 0.3)}')


class Coat(Clothes):

    def __init__(self, width, height):
        super().__init__(width, height)
        self.coat_pattern = round(self.width / 6.5 + 0.5)

    def __str__(self):
        return f'Fabric consumption for a coat = {self.coat_pattern}'


class Suit(Clothes):

    def __init__(self, width, height):
        super().__init__(width, height)
        self.suit_pattern = round(self.height * 2 + 0.3)

    def __str__(self):
        return f'Fabric consumption for a suit = {self.suit_pattern}'

coat = Coat(4, 6)
suit = Suit(2, 4)

print(coat)
print(suit)

print(coat.get_total_expense)
print(suit.get_total_expense)

print(coat.get_coat_pattern())
print(suit.get_suit_pattern())
