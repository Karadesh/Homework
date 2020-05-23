import random
my_list = [random.randrange(100) for i in range(10)]

print(my_list)
second_list = [el for el in my_list[:] if my_list.count(el) == 1]
print(second_list)
#my_list_2 = [2, 5, 5, 10,10]
#for i in my_list_2.index():
#    print(i)
#print(mylist_2)


#print(second_list)
