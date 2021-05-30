#Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
#В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
#преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года
#(например, месяц — от 1 до 12).
#Проверить работу полученной структуры на реальных данных.

class Date:
    def __init__(self, str_date):
        self.str_date = str_date

    @classmethod
    def date_digit(cls, param):
        list_d = param.split('-')
        list_d = list(map(int, list_d))
        return list_d

    @staticmethod
    def valid(param):
        if param[1] > 12:
            print('Неправильный месяц.')
        elif param[0] > 31 and [1, 3, 5, 7, 8, 10, 12].count(param[1]):
            print('Неправильное число.')
        elif param[0] > 30 and [4, 6, 9, 11].count(param[1]):
            print('Неправильное число.')
        elif param[0] > 28 and param[1] == 2:
            print('Неправильное число.')
        elif param[2] > 2021:
            print('Неправильный год.')
        else:
            print('Дата верна!')


print(Date.valid(Date.date_digit('20-08-1978')))
