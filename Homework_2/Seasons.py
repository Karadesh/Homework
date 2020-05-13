#3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.
winter = [12 , 1 , 2]
spring = [3 , 4 , 5]
summer = [6 , 7 , 8]
autumn = [9 , 10 , 11]
seasons = int(input ('введите номер месяца:'))
if seasons in winter:
    print('Это зима! Время лепить снеговика.')
elif seasons in autumn:
    print('Это осень! Завари кофе и садись у окна смотреть на дождь.')
elif seasons in spring:
    print('Это весна! Скоро лето!')
elif seasons in summer:
    print('Лето! Пора в отпуск!')
else:
    print('Вы знаете, сколько месяцев в году? 12!')


seasons_vault = {12 : 'Зима', 1 : 'Зима' , 2 : 'Зима' , 3 : 'Весна' , 4 : 'Весна' , 5 : 'Весна' , 6 : 'Лето' , 7 : 'Лето' , 8 : 'Лето' , 9 : 'Осень' , 10 : 'Осень' , 11 : 'Осень'}
seasons_second_task = int(input('Готов еще раз поиграть во времена года? Тогда введи число от 1 до 12: '))
if seasons_second_task in seasons_vault.keys():
    print(seasons_vault.get(seasons_second_task))
else:
    print('Вы знаете, сколько месяцев в году? 12!')