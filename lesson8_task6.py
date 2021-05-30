#Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
#Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

class Warehouse:
    warehouse = {}


class OfficeEquipment(Warehouse):
    def __init__(self, name, price):
        self.name = name
        self.price = price


    def to_warehouse(self, quantity):
        try:
            key = Warehouse.warehouse[self.name] + quantity
        except TypeError:
            print('Ошибка ввода.')
        else:
            Warehouse.warehouse[self.name] = key
            print(Warehouse.warehouse)

    def to_office(self, quantity):
        try:
            key = Warehouse.warehouse[self.name] - quantity
        except TypeError:
            print('Ошибка ввода.')
        else:
            Warehouse.warehouse[self.name] = key
            print(Warehouse.warehouse)


class Printer(OfficeEquipment):
    def __init__(self, name, price, weight):
        super().__init__(name, price)
        self.weight = weight
        Warehouse.warehouse[self.name] = 0


class Scanner(OfficeEquipment):
    def __init__(self, name, price, height):
        super().__init__(name, price)
        self.height = height
        Warehouse.warehouse[self.name] = 0


class Copier(OfficeEquipment):
    def __init__(self, name, price, length):
        super().__init__(name, price)
        self.length = length
        Warehouse.warehouse[self.name] = 0


brother = Printer('Brother', 1000, 5)
samsung = Scanner('Samsung', 1500, 10)
xerox = Copier('Xerox', 2000, 15)

brother.to_warehouse(5)
brother.to_office(3)
samsung.to_warehouse(10)
xerox.to_warehouse('50')
