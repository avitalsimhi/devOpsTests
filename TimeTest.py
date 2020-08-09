# import datetime


from datetime import datetime
print(datetime.now())

import array as arr
a = arr.array("i",[3,6,9])
# print(a[2])
# a[0] = 5
# print(a[0])
# a.append(10)
# a.pop(0)
# a.insert(1, 7)
# print(len(a))
for i in a:
    print(i)

for i in range(len(a)):
    print(a[i])

my_list = [5, "a", True]
print(my_list[2])

x_tuple = 1, 'b', 3, 'd', 5
print(x_tuple)
y_tuple = (1, 'b', 3, 'd')

my_dictionary = {"A": 1, "B": 2}
my_dictionary["A"] = 5
print(my_dictionary.keys())
print(my_dictionary.values())
del(my_dictionary["A"])
print(my_dictionary.keys())

