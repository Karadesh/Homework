#3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    def __init__(self, name, surname):
        self.name = str(name)                           #Переводим в строку.
        self.surname = str(surname)
        self._income = {'wage': 1000, 'bonus': 500}             #Создаем словарь income


class Position(Worker):
    def worker_position(self):
        get_full_name = (f'{self.name} {self.surname}')             #Для вывода имени и фамилии.
        a = (self._income.get('wage'))                              #Присваиваем значения переменной для удобного подсчета.
        b = (self._income.get('bonus'))
        get_total_income = a + b
        return ([get_full_name,get_total_income])                   #Возвращаем списком имя, фамилию и зарплату.


worker_prize = Position('a','b')
print(worker_prize.worker_position())