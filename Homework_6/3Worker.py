class Worker:
    def __init__(self, name, surname):
        self.name = str(name)
        self.surname = str(surname)
        self._income = {'wage': 1000, 'bonus': 500}


class Position(Worker):
    def worker_position(self):
        get_full_name = (f'{self.name} {self.surname}')
        a = (self._income.get('wage'))
        b = (self._income.get('bonus'))
        get_total_income = a + b
        return ([get_full_name,get_total_income])


worker_prize = Position('a','b')
print(worker_prize.worker_position())