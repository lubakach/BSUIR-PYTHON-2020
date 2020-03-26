import math


class Vector:
    # конструктором класса - метод, который автоматически вызывается при создании объектов
    def __init__(self, *num):  # первый параметр всегда self
        if len(num) == 0:  # если нет переменных
            self.values = (0, 0)
        else:
            self.values = num  # передает значение num

    def addition(self, vector2):
        # tuple - кортеж, неизменяемый список
        # zip - позволяет пройтись по нескольким итерируемым объектам
        result = tuple(a + b for a, b in zip(self.values, vector2.values))
        return Vector(*result)

    def subtraction(self, vector2):
        result = tuple(a - b for a, b in zip(self.values, vector2.values))
        return Vector(*result)

    def multiplication(self, num):  # умножение на число
        result = tuple(a * num for a in self.values)
        return Vector(*result)

    def multiplication_vectors(self, vector2): # умножение двух объектов
        multiplication = tuple(a * b for a, b in zip(self.values, vector2.values))
        result = 0
        for i in multiplication:
            result += i
        return result

    def equality(self, vector2):  # сравнение
        for a, b in zip(self.values, vector2.values):
            if a != b:
                return False
        return True

    def length(self):
        result = 0
        for i in self.values:
            result += i**2
        result = math.sqrt(result)
        return result


if __name__ == "__main__":
    vector_1 = Vector(11, 6, 7)
    vector_2 = Vector(2, 2, 2)
    vector_3 = vector_1
    print("First: ", vector_1.values)
    print("First[1]: ", vector_1.values[1])
    print("Second: ", vector_2.values)
    print("Subtraction first and second: ", vector_1.subtraction(vector_2).values)
    print("Addition first and second: ", vector_1.addition(vector_2).values)
    print("Multiplication First x 3: ", vector_1.multiplication(3).values)
    print("Equality First x Second: ", vector_1.equality(vector_2))
    print("Equality First and Third: ", vector_1.equality(vector_3))
    print("Multiplication by vectors: ", vector_1.multiplication_vectors(vector_3))
    print("Length: ", (vector_1.length()))
