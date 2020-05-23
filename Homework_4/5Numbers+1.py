#1.

from itertools import count,cycle

for i in count(int(input('Введите начальное число: '))):
    print(i)

#2.

repeat_this_list = [2 , 3 , 5 , 10 , 25 , 156 , 15 , 35 , 2 , 10]

end_of_repeat = ''
iter = cycle(my_list)
while end_of_repeat != 'q':
    print(next)