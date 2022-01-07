my_dict = {'a': 100, 'b':200, 'c':300}
my_list = []
for i in my_dict:
    my_list.append(my_dict[i])
final_sum = sum(my_list)
print("The sum of the values in the dictionary is: ",final_sum)