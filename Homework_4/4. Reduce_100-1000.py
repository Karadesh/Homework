#4. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
from functools import reduce

elements_of_thousand = [el for el in range(100,1000) if el %2 == 0]         #Выводим элемент из четных чисел в диапазоне от 100 до 1000
even_numbers = reduce(lambda x , y : x * y, elements_of_thousand)           #Через lambda высчитываем умножение каждого следующего числа
print(even_numbers)
#print(elements_of_thousand)

#print(division_of_thousands)