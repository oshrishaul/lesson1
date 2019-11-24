# list[] vs tuple()
my_list = ["pi", 3.14,True]
my_tuple = ("pi", 3.14,True)

# We can edit list[]
my_list.append(False)
my_list[2] = "false"

# #But can not edit a tople() !!!!

# for a in my_list:
#     print(a)
#
# for a in my_tuple:
#     print(a)

# Dictionary{}
# my_dic = {"name":"oshri", "age":27, "man":True}
#
# print(my_dic["name"])
# print(my_dic["age"])
# print(my_dic["man"])
# print(my_dic.keys())
# print(my_dic.values())

my_street = [("dizingof",1), ("dizingof",2), ("dizingof",3)]
my_dict = {my_street[0]:10, my_street[1]:20, my_street[2]:15}

for building in my_street:
    print(my_dict)
    print(my_street)
    print(building)
    print(my_dict[building])

    print("there are", my_dict[building], "families", "in", building)


