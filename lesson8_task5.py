#Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и
#передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
#а также других данных, можно использовать любую подходящую структуру, например словарь.

class Warehouse:
    warehouse = {}


class OfficeEquipment(Warehouse):
    def __init__(self, name, price):
        self.name = name
        self.price = price


    def to_warehouse(self, quantity):
        key = Warehouse.warehouse[self.name] + quantity
        Warehouse.warehouse[self.name] = key
        print(Warehouse.warehouse)

    def to_office(self, quantity):
        key = Warehouse.warehouse[self.name] - quantity
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
xerox.to_warehouse(12)
