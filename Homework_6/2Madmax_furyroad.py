#2. Реализовать класс Road (дорога), в котором определить атрибуты:
# length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
#Например: 20м * 5000м * 25кг * 5см = 12500 т

class Road:
    def __init__(self, length, width):
        self._length = int(length)              #Переводим значения в интовые(на всякий случай).
        self._width = int(width)
        asfalt_mass_for_santimeter = 20         #Количество сантиметров асфальта - константа.
        asfalt_fat = 30                         #Толщина на 1 см.
        total_mass = width * length * asfalt_fat * asfalt_mass_for_santimeter   #Формула
        print(total_mass)                                                       #Выводим итог формулы.
#        return total_mass

mass_of_asphalt = Road(20,30)





