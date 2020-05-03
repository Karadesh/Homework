#4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number = int(input('Введите целое положительное число: '))
bigest_number = number % 10
while number / 10 >= 1:
    number = number / 10
    if number %10 >= bigest_number:
        bigest_number = number %10

print('Наибольшая цифра: ', int(bigest_number))

