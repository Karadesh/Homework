from itertools import count
from math import factorial

def cycle_gen():
    for el in count(1):
        yield factorial(el)


numbers = 0
for i in cycle_gen():
    print('Factorial from {} is {}'.format(numbers + 1 , i))
    if numbers == 14:
        break
    numbers = numbers + 1