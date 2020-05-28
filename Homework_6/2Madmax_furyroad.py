class Road:
    def __init__(self, length, width):
        self._length = int(length)
        self._width = int(width)
        asfalt_mass_for_santimeter = 20
        asfalt_fat = 30
        total_mass = width * length * asfalt_fat * asfalt_mass_for_santimeter
        print(total_mass)
#        return total_mass

mas = Road(20,30)
#print(mas)




