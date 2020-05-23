from sys import argv

script_name, money, hours, prize = argv

money = int(money)
hours = int(hours)
prize = int(prize)
workers_prize = money * hours + prize

print(f'Зарплата работника равна: {workers_prize} золотых монет.')