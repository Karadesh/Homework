#2a. Представлен список чисел.
# Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
#Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
# Для формирования списка использовать генератор.
#Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
#Результат: [12, 44, 4, 10, 78, 123].
import random
my_list = [random.randrange(100) for i in range(10)]            #Заполняем список случайными значениями
print(my_list)

second_list =[my_list[i+1] for i in range(len(my_list) - 1) if my_list[i+1] > my_list[i]]   #Заполняем второй список элементами, со значением большим, чем предыдущий

print(second_list)                  #Выводим

#2b (В методичке 3)
#Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21.
# Необходимо решить задание в одну строку.
#Подсказка: использовать функцию range() и генератор.

third_list = [el_1  for el_1 in range(20,240) if el_1 %20 == 0 or el_1 %21 ==0]   #Смотрим по каждому элементу с 20 до 240: делится ли оно на 20 или 21.
print(third_list)
