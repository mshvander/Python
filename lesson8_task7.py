#Реализовать проект «Операции с комплексными числами».
#Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
#Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
#Проверьте корректность полученного результата.

class ComplexNumber:
    def __init__(self, real, imaginary):
        self.n = [real, imaginary]

    def __str__(self):
        if self.n[1] > 0:
            return f'Комплексное число ({self.n[0]} + {self.n[1]}i)'
        else:
            return f'Комплексное число ({self.n[0]} - {abs(self.n[1])}i)'

    def __add__(self, other):
        return ComplexNumber((self.n[0] + other.n[0]), (self.n[1] + other.n[1]))

    def __mul__(self, other):
        return ComplexNumber((self.n[0] * other.n[0] - self.n[1] * other.n[1]), (self.n[0] * other.n[1] + self.n[1] * other.n[0]))


a = ComplexNumber(4, 5)
b = ComplexNumber(7, -1)

print(a)
print(b)

print(a + b)
print(a * b)
