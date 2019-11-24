# A.
# 1. Create two variables name X and Y.
# 2. Print “BIG” if X is bigger than Y .
# 3. Print “small” if X is smaller than Y.
x=1
y=2
if x>y:
    print("BIGGER")
else:
    print("small")

# B.
# 1. Run a “for” loop 5 times.
# 2. Print iteration number every time.

for a in range(5):
    print(a)

# C.
# 1. Create a variable and initialize it with a number 1-4.
# 2. Create 4 conditions (if-elif) which will check the variable.
# 3. print the season name accordingly:
# - 1 = summer
# - 2 = winter
# - 3 = fall
# - 4 = spring
seasone = 3
if seasone == 1:
    print("Summer")
elif seasone == 2:
    print("Winter")
elif seasone == 3:
    print("Fall")
elif seasone == 4:
    print("Spring")

# D. Given the following loop:
# ================
# count = 1
# while count<11:
# print(count)
# count = count+1
# =================
# 1. how many times will the following loop run?
# Answer 1. The following loop will run 10 times, starting from 1 to 10
# 2. what will be printed last?
# Answer 2. The last print will be '10'

# E.
# Write a program with variables holding the following:
# 1. Your age.
# 2. First letter of your last name.
# 3. Current shekels-dollar currency.
# 4. Did you flew abroad (true/false)
# 5. Your apartment number.
# ● Print all variables.
# ● Add the currency to your age, and check the result.
age=27
first='s'
currency=3.5341
flew=True
apartment=184
print(age,'\n',first,'\n', currency,'\n', flew,'\n',apartment)
print(age+currency)

# F.
# Create a program which uses input with the following:
# 1. Ask user for his phone number
# 2. Print the words “phone number” and the phone number the user entered.
phone = input("Please type in your phone number")
print("Phone number", phone)

# G.
# Write a program with the following:
# 1. Method named printHello() that prints the word “hello”.
# 2. Method named calculate() which adds 5+3.2 and prints the
# result.
def printHello():
    print("hello")
def calculate():
    print(5+3.2)
# H.
# Write a program with the following:
# 1. Method that receive your name and prints it.
# 2. Method that receive a number, divide it by 2, and prints the result.
def your_name(name):
    print(name)
def divide(number):
    print(number / 2)

# I.
# Write a program with the following:
# 1. Method that receive two numbers, add them, and return the sum
# 2. Method that receive two Strings, add space between them, and return one spaced string.

def sum2(num1,num2):
    return num1+num2
def space_strings(string1,string2):
    return string1 + " " + string2

# J.
# Create a program with the following:
# 1. Create an array with 3 numbers
# 2. Iterate through the array to print all elements.
import array as my_arr
z = my_arr.array("i", [2,4,6])
for x in z:
    print(x)









