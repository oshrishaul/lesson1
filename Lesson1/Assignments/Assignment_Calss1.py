print("**** A - START ****")
# Create a program with the following:
# A:
# 1. Create a variable name "first" with value '7'.
first = 7
# 2. Create a variable name second with value 44.3.
second = 44.3
# 3. Print result of adding first to second.
print(first + second)
# 4. Print result of multiplying first by second
print(first * second)
# 5. Print result of dividing second by first
print(second / first)

print("**** A - END ****")

print("**** B - START ****")
# B.
# What will be the values of a, b, c at the end
a=8
a=17
a=9
b=6
c= a+b
b = c+a
b=8
print("a =", a)
print("b =", b)
print("c =", c)
print("**** B - END ****")

print("**** C - START ****")
# C.
# Is there a difference between the two lines below? Why?
# name = "john"
# name = 'john'
# NO, we can use them both to define a string.
#But! if you want to use the single quote in your string you have to use the double quotes to define your string. for example:
# car = "john's car is red"

# What is the issue with the code below?  Suggest an edit.
my_number = 5+5
# print("result is: "+my_number)
# Since we insert a calculation to "my_number" the Pycharm used it as integer. so we need to use 'int' before "my_number" to make 'print' action works as expected. integer we need to use 'int' before "my_number for
# Suggested solution
print("result is: "+str(my_number))
print("**** C - END ****")

print("**** D - START ****")
# D.
# What will be the output of the following code?
x=5
y=2.36
print(x+int(y))
print("The output will be 7 instead of 7.36 because we insert a floating point number to 'y'")
print("Suggested solution - use 'float' instead of 'int'  ==>> print(x+float(y)")
print("**** D - END ****")

print("**** E - START ****")
# E.
# 1. Create two variables name X and Y.
X=4
Y=8
# 2. Print “BIG” if X is bigger than Y .
# 3. Print “small” if X is smaller than Y.
if X > Y:
    print("BIG")
else:
    print("small")
print("**** E - END ****")

print("**** F - START ****")
# F.
# 1. Create a variable and initialize it with a number 1-4.
# 2. Create 4 conditions (if-elif) which will check the variable.
# 3. print the season name accordingly:
# - 1 = summer
# - 2 = winter
# - 3 = fall
# - 4 = spring
# In case that user intervention was required use the following command instead:
# season = int(input("pleas choose a number between 1-4"))
season = 4
if season == 1:
    print("summer")
elif season == 2:
    print("winter")
elif season == 3:
    print("fall")
elif season == 4:
    print("spring")
print("**** F - END ****")

# Challenge - Fix the following code, without changing a or b
a = 8
b = "123"
print(a+int(b))
