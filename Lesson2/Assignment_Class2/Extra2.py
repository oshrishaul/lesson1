# # Create a nested for loop to create X shape (width is 7, length is 7):
# i=0
# j=4
# for row in range(5):
#     for col in range(5):
#         if row==i and col==j:
#             print("*",end="")
#             i=i+1
#             j=j-1
#         elif row==col:
#             print("*",end="")
#         else:
#             print(end=" ")
#     print()

# x=0
# y=0
# for row in range(5):
#     for col in range(5):
#
# print()
# n = 5
for i in range(0, 5):

    # inner loop to handle number of columns
    # values changing acc. to outer loop
    for j in range(0, i + 1):
        # printing stars
        print("* ", end="")

        # ending line after each row
    print("\r")

# Driver Code
