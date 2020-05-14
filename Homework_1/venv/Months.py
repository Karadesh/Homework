#2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

elements = []
elements_second = []
count = 0
a = abs((int(input('Введите количество символов списка: ')))) #Пользователь вводит количество элементов списка
while len(elements) != a:
   elements.append((input('Введите символ для заполнения списка: '))) #Забиваем список элементами, которые введет пользователь
for element in elements[:]:
    if count %2 == 0 and count < (a - 1):      #Добавляем условие деления без остатка на 2 условие, при котором мы не выйдем из списка elements
        elements_second.append(elements[count + 1])
        count = count + 1
    elif count %2 != 0 and count < a:
        elements_second.append(elements[count - 1])
        count = count + 1
    else:
        elements_second.append(elements[a - 1])            #Запоминаем последний элемент списка
        break
print(elements_second)