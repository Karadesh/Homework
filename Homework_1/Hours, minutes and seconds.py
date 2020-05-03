#2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

seconds = int(input('Введите количество секунд: '))
minutes = int(seconds/60)
hours = int(minutes/60)
seconds = seconds - (minutes*60)
minutes = minutes - (hours*60)
print('У нас получилось: {}:{}:{}'.format(hours , minutes, seconds))