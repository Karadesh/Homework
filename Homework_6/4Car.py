import time
from itertools import count

class Car:
    def __init__(self,speed,color,name,is_police):
        self.speed = speed
        self.color = color
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
        direction = ['Вправо', 'Влево']
        for timer in range(10):
            for i in direction:
                print(f'Машина поехала {i}')
                self.speed = self.speed + 1
 #               time.sleep(1)
    def show_speed(self):
          print(f'Скорость: {self.speed}')
          self.result.append(self.speed)

class TownCar(Car):
    def show_speed(self):
        self.result.append(self.speed)
        if self.speed > 60:
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


mar = PoliceCar(50,'red','Sport',False)
mar.turn()
mar.show_speed()
print(mar.result)