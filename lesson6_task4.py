#Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
#А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
#Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
#Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
#Для классов TownCar и WorkCar переопределите метод show_speed.
#При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Автомобиль {self.name} поехал.')

    def stop(self):
        print(f'Автомобиль {self.name} остановился.')

    def turn(self, direction):
        print(f'Автомобиль {self.name} повернул {direction}')

    def show_speed(self, current_speed):
        print(f'Текущая скорость автомобиля {self.name} составляет {current_speed} км/ч.')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self, current_speed):
        print(f'Текущая скорость автомобиля {self.name} составляет {current_speed} км/ч.')
        if current_speed > 60:
            print('Скорость превышена!')

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self, current_speed):
        print(f'Текущая скорость автомобиля {self.name} составляет {current_speed} км/ч.')
        if current_speed > 40:
            print('Скорость превышена!')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


lada = Car(110, 'green', 'Lada', False)
lincoln = TownCar(150, 'silver', 'Lincoln', False)
ferrari = SportCar(300, 'red', 'Ferrari', False)
ford = WorkCar(130, 'orange', 'Ford', False)
uaz = PoliceCar(120, 'blue', 'UAZ', True)

lada.go()
lincoln.go()
lada.show_speed(89)
ford.show_speed(75)
uaz.turn('направо')
