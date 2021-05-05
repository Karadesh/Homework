'''
p = "3-12-25"
a = p.split("-")
hours = int(a[0])
minutes = int(a[1])
seconds = int(a[2])

print(hours, minutes, seconds)
'''

#1


class Data:
    def __init__(self, date_string):
        self.date_string = str(date_string)

    @classmethod
    def str_to_int(cls, date_string):
        date = []
        for i in date_string.split():
            if i != '-':                     #создаем список, в который помещаем полученные после
                date.append(i)                  #split значения и возвращаем их в виде int
        return int(date[0]), int(date[1]), int(date[2])
    
    @staticmethod
    def validator(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 9999 >= year >= 0:
                    return f"validation is succesfull"
                else:
                    return "please type correct year"       #через цикл if проверяем значения
            else:
                return "please type correct month"
        else:
            return "please type correct day of month"

    def __dir__(self):
        return f"date is: {Data.str_to_int(self.date_string)}"


date_1 = Data("21 - 05 - 2019")
print(date_1.str_to_int("21 - 05 - 2019"))
print(Data.validator(20, 10, 2015))


#2


class ZeroDivError(Exception):
    def __init__(self, arg_1, arg_2):
        self.arg_1 = arg_1
        self.arg_2 = arg_2

    @staticmethod
    def division_on_zero(arg_1, arg_2):
        try:
            return arg_1 / arg_2
        except ZeroDivisionError:
            return f"you can't divide by zero"


print(ZeroDivError.division_on_zero(10, 0))


#3


class Int_validator(Exception):
    def __init__(self, text, *args):
        self.txt = text
        self.user_list = []

    def list_validation(self):
        while True:
            try:
                asker = int(input('Type digits and Enter then:'))
                self.user_list.append(asker)
                print(f'list now is {self.user_list}')
            except:
                print("only int enabled")
                answer = input("try again? Yes or No")
                if answer.title() == "Yes":
                    print(p.list_validation())
                else:
                    print(f'ok then. Your list is {self.user_list}')
                    break



p = Int_validator(2)
p.list_validation()
p.user_list



# 4,5,6


class Warehouse:

    def __init__(self, name, quantity, working_speed, price):
        self.name = name
        self.quantity = quantity
        self.working_speed = working_speed
        self.price = price
        self.stack = []
        self.full_stack = []
        self.stack_unit = {'name': self.name, 'quantity': self.quantity, 'speed': self.working_speed, 'price': self.price}

    def __str__(self):
        return f'{self.name} price is {self.price}, quantity is {self.quantity}'

    def warehouse_stacker(self):
        try:
            unit = input('type name of tech: ')
            unit_price  = float(input('type price of tech: '))
            unit_quantity = int(input('type quantity: '))
            unit_speed = float(input('type speed of tech: '))
            unit_stack = {'name': unit, 'quantity': unit_quantity, 'speed': unit_speed, 'price': unit_price}
            self.stack_unit.update(unit_stack)
            self.stack.append(self.stack_unit)
            print(f'now store is: \n {self.stack}')
        except:
            return 'data error!'
        q = input('for exit type q, enter to continue')
        if q.title() == "Q":
            self.full_stack.append(self.stack)
            print(f'this is warehouse: {self.full_stack}')
            return 'exit'
        else:
            return Warehouse.warehouse_stacker(self)


class Printer(Warehouse):
    def printing(self):
        return "printing!"


class Scanner(Warehouse):
    def scanning(self):
        return "scanning!"


class Xerox(Warehouse):
    def copying(self):
        return "i'm actually copier. Ok. copying!"


r = Printer('hp', 2000, 5, 10)
p = Scanner('rawr', 2000, 3, 5)
g = Xerox('arthas', 300, 5, 10)
print(r.warehouse_stacker())


#7

class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.c = 'a + b * i'

    def __add__(self, other):
        return f'sum of first number and second is:  {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        return f'multiply is: {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'z = {self.a} + {self.b} * i'


first = Complex(1, -10)
second = Complex(3, 5)
print(first)
print(first + second)
print(first * second)
