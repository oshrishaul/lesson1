# Check if a number is bigger than 500 AND even number, than print it. ignore the odd numbers.

# my_list = [10,2,20,34,35,60,61,90,78,77,45,40,504,6,8]
# for a in my_list:
#     if a > 500:
#         print(a,"is bigger than 500")
#         continue
#     if a % 2 == 0:
#         print(a, "is an even number")

#כתוב פונקציה שמקבלת ליסט, ומחזירה את סכום כל המחרוזות של הליסט
my_list = [1,3,56,78,90,100,11]
def sum_list(list):
    print(len(list))

sum_list(my_list)

hob_list = ["soccer", "basketball", "tennis"]
dict_3 = {"name":27, "age":27, "hobbies":hob_list}

def dict_validatore(a_dict):
    #{'name':string, 'age':number, 'hobbies':list}
    if not type(a_dict['name']) is str:
        print("name is not a string")
    if not type(a_dict['age']) is int:
        print("age is not a number")
    if not type(a_dict['hobbies']) is hob_list:
        print("hobbies error")

dict_validatore(dict_3)