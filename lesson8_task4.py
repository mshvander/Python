#Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
#А также класс «Оргтехника», который будет базовым для классов-наследников.
#Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
#В базовом классе определить параметры, общие для приведенных типов.
#В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

class Warehouse:
    def __init__(self, name):
        self.name = name


class OfficeEquipment:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Printer(OfficeEquipment):
    def __init__(self, name, price, weight):
        super().__init__(name, price)
        self.weight = weight


class Scanner(OfficeEquipment):
    def __init__(self, name, price, height):
        super().__init__(name, price)
        self.height = height


class Copier(OfficeEquipment):
    def __init__(self, name, price, length):
        super().__init__(name, price)
        self.length = length
