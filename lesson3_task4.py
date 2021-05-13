#Программа принимает действительное положительное число x и целое отрицательное число y.
#Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
#При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
#Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
#Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

def my_func(x, y):
    '''Возводит x в степень y с помощью цикла'''
    res = 1
    for i in range(abs(y)):
        res = res / x
    return res

x = float(input('Введите действительное положительное число: '))
y = int(input('Введите целое отрицательное число: '))

print((lambda x, y: x ** y) (x, y))
print(my_func(x, y))




