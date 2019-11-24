# *************** Python Loops ***************
# for a in range(5):
#     print(a)
# # range(start point, end point, jumps)
#
# count = 5
# while count < 10:
#     print(count)
#     count += 1 #this is the same as - count +1

# for a in range(1,10):
#     if a % 2 == 0:
#         print(a)
#         # break
#     else:
#         print("not an even number")
# print("out of scope")

# for a in range (10):
#     if a % 2 == 0:
#         print("in if scope")
#         continue
#     print(a)
# print("out of scope")

# #print a specific location
# my_list = [10,2,20,34,35,60,61,90,78,77,45,40,504,6,8]
# print(my_list[3])

# לחזור על מודולים !!!!

# count = 1
# while count<11:
#     print(count)
#     count = count+1
# import array
# arr = array.array('i', [2, 4, 6])
# print ("The new created array is : ",end=" ")
# for i in range(0, 3):
#     print(arr[i], end=" ")
# print("\r")

# import array as add
# if __name__ == "__main__":
#     a = add.array("i",[3,6,9])
#     for temp_num in a:
#         print(temp_num)

import array as my_arr
a = my_arr.array("i", [2,4,6])
for temp in a:
    print(temp)




















