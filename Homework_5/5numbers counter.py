#5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
from itertools import count

with open('Numbers_counter.txt', 'w') as numbers_counter:
    numbers_counter.write('12 34 52 62 62 52')                #Создаем файл и вводим в него числа через пробел.
numbers_counter.close()
numbers_counter = open('Numbers_counter.txt', 'r')
sum_of_i = 0                                                  #Переменная для хранения суммы чисел.
for i in numbers_counter:
        spliter = i.split( )                                  #создаем список из чисел в файле
for number in spliter:
    number = int(number)                                      #Превращаем каждый элемент списка в целое число
    sum_of_i = sum_of_i + number
print(sum_of_i)                                               #Складываем числа списка и выводим на экран.
numbers_counter.close()

