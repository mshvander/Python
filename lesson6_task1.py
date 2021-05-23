#Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
#Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
#Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
#Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
#Проверить работу примера, создав экземпляр и вызвав описанный метод.

import time

class TraficLight:
    __color = None

    def running(self, red_time, yellow_time, green_time):
        self.__color = 'Красный'
        print(f'Загорается {self.__color} свет.')
        time.sleep(red_time)
        self.__color = 'Желтый'
        print(f'Загорается {self.__color} свет.')
        time.sleep(yellow_time)
        self.__color = 'Зеленый'
        print(f'Загорается {self.__color} свет.')
        time.sleep(green_time)


ul_tverskaya = TraficLight()
ul_tverskaya.running(7, 2, 15)
