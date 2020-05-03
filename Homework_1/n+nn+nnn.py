#3. Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.

primordial_number = str(input('Введите цифру: '))
number_two = int('{}{}'.format(primordial_number,primordial_number))
number_three = int('{}{}'.format(primordial_number,number_two))
primordial_number = int(primordial_number)
numbers_sum = (primordial_number + number_two + number_three)
print(numbers_sum)