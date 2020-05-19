#3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def sum_of_bigest_numbers(a , b , c):
    base_of_numbers = []
    base_of_numbers.append(a)          #Заполняем пустой список введенными числами
    base_of_numbers.append(b)
    base_of_numbers.append(c)
    first_of_sum = 0
    second_of_sum = 0                   #Задаем 2 переменные, которые в дальнейшем будут складываться
    for i in base_of_numbers:           #Сравниваем первую переменную с каждым элементом списка
        if first_of_sum <= i:
            second_of_sum = first_of_sum    #Если переменная меньше элемента списка, присваиваем ей значение этого элемента
            first_of_sum = i                #Второй переменной - предыдущее значение первой.
    return first_of_sum + second_of_sum



first_number = int(input('Введите первое число: '))
second_number = int(input('Введите второе число: '))
third_number = int(input('Введите третье число: '))

result = sum_of_bigest_numbers(first_number , second_number , third_number)
print(result)