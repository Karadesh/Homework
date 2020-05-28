#4. Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

import time                                             #Вызываем, чтобы машина поворачивала через определенное время.

class Car:
    def __init__(self,speed,color,name,is_police):
        self.speed = speed                              #создаем атрибуты и список, который будет выводиться в конце
        self.color = color                              #программы.
        self.name = name
        self.is_police = is_police
        self.result = []
        self.result.append(self.color)
        self.result.append(self.name)
        self.result.append(self.is_police)

    def go(self):
        print('Машина поехала!')

    def stop(self):
        print('Машина остановилась!')

    def turn(self):
        direction = ['Вправо', 'Влево']                 #Список поворотов.
        for timer in range(10):                         #Для остановки поворотов.
            for i in direction:
                print(f'Машина поехала {i}')
                self.speed = self.speed + 1             #Увеличиваем скорость после каждого поворота.
 #               time.sleep(1)                          #Машина поворачивает через 1 секунду (закомментировано для удобства чтения).

    def show_speed(self):
          print(f'Скорость: {self.speed}')
          self.result.append(self.speed)                #Добавляем в список скорость.

class TownCar(Car):
    def show_speed(self):
        self.result.append(self.speed)
        if self.speed > 60:                             #Условие вывода сообщения.
            print('Скорость превышена!')

class SportCar(Car):
    def show_speed(self):
        self.result.append(self.speed)
        if self.speed > 60:
            print('Это спорткар, детка! Поедем с ветерком!')

class WorkCar(Car):
    def show_speed(self):
        self.result.append(self.speed)
        if self.speed > 40:
            print('Скорость превышена')

class PoliceCar(Car):
    def show_speed(self):
        self.result.append(self.speed)
        print('По машинам! Пора ловить преступников!')


mar = PoliceCar(50, 'red', 'Sport', True)
mar.turn()
mar.show_speed()
print(mar.result)