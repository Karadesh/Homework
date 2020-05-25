#3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

workers_data = {}                                  #Создаем словарь, где будут хранится ключи (фамилии) и значения (сумма)
file_opener = open('Workers_data.txt', 'r')
for line in file_opener:
    worker = line.split( )                         #Создаем список формата ['Имя' , 'Сумма']
    workers_data[worker[0]] = int(worker[1])       #Делаем сумму int и добавляем ключ и значение в словарь workers_data
best_worker = 0                                     #Переменная для подсчета среднего
counter = 0                                         #Переменная для количества сотрудников
for key, value in workers_data.items():
    best_worker = best_worker + value               #Добавляем в переменную best_worker сумму оклада каждого сотрудника
    counter = counter + 1                           #После каждого пройденного сотрудника запоминаем его в counter
    if value > 20000:                               #Цикл для вывода на экран работников, чей оклад больше 20 000 рублей
        print(key)
print(best_worker / counter)                        #Выводим среднее значение зп всех сотрудников






#    for i in workers_base:

#    workers_data = dict.fromkeys(workers_base,workers_base[1])
#    print(workers_data)
#print(workers_base)