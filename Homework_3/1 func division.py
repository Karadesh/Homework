#1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def division(a,b):
     if b == 0:                     #Заглушка для деления на 0
         return 'На ноль делить нельзя'
     return a / b


first_number = float(input('Введите первое число: '))
second_number = float(input('Введите второе число: '))

devision_result = division(first_number,second_number)

print(devision_result)