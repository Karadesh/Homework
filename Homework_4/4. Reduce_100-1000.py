from functools import reduce

elements_of_thousand = [el for el in range(100,1000) if el %2 == 0]
even_numbers = reduce(lambda x , y : x * y, elements_of_thousand)
print(even_numbers)
#print(elements_of_thousand)

#print(division_of_thousands)