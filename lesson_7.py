'''
class MyClass:
    def __init__(self, param):
        self.param = param

    def __add__(self, other):
        return MyClass(self.param + other.param)

    def __str__(self):
        return f"object with param ({self.param})"

    def __del__(self):
        print(f"deleting object {self.param} of MyClass")


mc_1 = MyClass("concatenate ")
mc_2 = MyClass("text")
print(mc_1 + mc_2)




class MyClass:
    def __setattr__(self, attr, value):
        self.__dict__[attr] = value


mc = MyClass()
mc.width = 40
mc.defence = 35
print(mc.width)
print(mc.defence)




class Class1:
    def __init__(self, param):
        self.param = param

    def __call__(self, newparam):
        self.param = newparam

    def __str__(self):
        return str(self.param)


class Class2:
    def __init__(self, *args):
        self.my_list = []
        for el in args:
            self.my_list.append(Class1(el))

    def __getitem__(self, index):
        return self.my_list[index]


my_obj = Class2(10, True, "text")
print(my_obj.my_list[1])
print(my_obj[1])



class MyClass:
    def __init__(self):
        self.x = 40

    def __eq__(self, y):
        return self.x == y


mc = MyClass()
print(mc == 40)



class Parent:
    def __init__(self):
        print("rawr parent")

    def my_method(self):
        print("parent method")


class Child(Parent):
    def __init__(self):
        print("child")
        super().__init__()

    def my_method(self):
        print("child method")
        super().my_method()


c = Child()
c.my_method()


class Iterator:
    def __init__(self, start=0):
        self.i = start - 1

    def __iter__(self):
        return self

    def __next__(self):
        self.i += 1
        if self.i <= 5:
            return self.i
        else:
            raise StopIteration


obj = Iterator(2)
for el in obj:
    print(el)



class Auto:
    def __init__(self, year):
        self.year = year

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        if year < 2000:
            self.__year = 2000
        elif year > 2019:
            self.__year = 2019
        else:
            self.__year = year

    def get_auto_year(self):
        return f"auto in {str(self.year)}"


a = Auto(2090)
print(a.get_auto_year())
'''

#1


class Matrix:
    def __init__(self, user_matrix):
        self.user_matrix = user_matrix

    def __str__(self):
        return '\n'.join([' '.join([str(elem) for elem in line]) for line in self.user_matrix])

    def __add__(self, other):
        total = ''
        if len(self.user_matrix) == len(other.user_matrix):
            for line1, line2 in zip(self.user_matrix, other.user_matrix):
                if len(line1) != len(line2):
                    return "please type correct size of matrix"

                matrix_line = [x + y for x, y in zip(line1, line2)]
                total += ' '.join([str(i) for i in matrix_line]) + '\n'
        else:
            return "please type correct size of matrix"
        return total


p_1 = Matrix([[1, 2], [3, 4], [5, 6]])
p_2 = Matrix([[3, 4], [2, 1], [9, 2]])
print(p_1 + p_2)

#2

from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, parameter):
        self.parameter = parameter

    @abstractmethod
    def calculate(self):
        pass


class Coat(Clothes):

    @property
    def calculate(self):
        return round((self.parameter / 6.5) + 0.5)


class Costume(Clothes):

    @property
    def calculate(self):
        return round((2 * self.parameter) + 0.3)


coat = Coat(30)
costume = Costume(120)
print(coat.calculate)
print(costume.calculate)

#3


class Cage:
    def __init__(self, nums):
        self.nums = nums

    def orders(self, rows):
        return '\n'.join(['*' * rows for _ in range(self.nums // rows)]) + '\n' + '*' * (self.nums % rows)

    def __str__(self):
        return str(self.nums)

    def __add__(self, other):
        return str(self.nums + other.nums)

    def __sub__(self, other):
        return self.nums - other.nums if self.nums - other.nums > 0 \
            else "too much dots on second cage or they're equal"

    def __mul__(self, other):
        return str(self.nums * other.nums)

    def __truediv__(self, other):
        return self.nums / other.nums if other.nums != 0 \
            else "you cannot divide on 0"


cage_1 = Cage(20)
cage_2 = Cage(40)
print(cage_1)
print(cage_1 + cage_2)
print(cage_1.orders(5))
