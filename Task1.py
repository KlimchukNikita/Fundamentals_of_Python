# 1. Реализовать класс Matrix (матрица).
# Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
#
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов
# класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.

class Matrix:

    def __init__(self, some_list_1, some_list_2):
        self.some_list_1 = some_list_1
        self.some_list_2 = some_list_2

    def __add__(self):
        some_matrix = [[0, 0, 0],
                       [0, 0, 0],
                       [0, 0, 0]]

        for i in range(len(self.some_list_1)):

            for j in range(len(self.some_list_2[i])):
                some_matrix[i][j] = self.some_list_1[i][j] + self.some_list_2[i][j]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in some_matrix]))

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in some_matrix]))


great_matrix = Matrix([[1, 2, 3],
                       [4, 5, 6],
                       [7, 8, 9]],
                      [[1, 2, 3],
                       [4, 5, 6],
                       [7, 8, 9]])

print(great_matrix.__add__())
