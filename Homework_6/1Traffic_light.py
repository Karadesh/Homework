from itertools import count
import time
class TrafficLight:
    def __init__(self):
        traffic = self.__color()
        return traffic


    def __color(self):
        color = ['Красный', 'Желтый', 'Зеленый']
        for timer in count():
            for i in color:
                print(i)
                if i == 'Красный':
                    time.sleep(7)
                elif i == 'Желтый':
                    time.sleep(2)
                elif i == 'Зеленый':
                    time.sleep(4)




traffic_light = TrafficLight()
print(traffic_light)



