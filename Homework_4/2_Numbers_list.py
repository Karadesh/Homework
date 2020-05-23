import random
my_list = [random.randrange(100) for i in range(10)]
print(my_list)

second_list =[my_list[i+1] for i in range(len(my_list) - 1) if my_list[i+1] > my_list[i]]

print(second_list)


third_list = [el_1  for el_1 in range(20,240) if el_1 %20 == 0 or el_1 %21 ==0]
print(third_list)
