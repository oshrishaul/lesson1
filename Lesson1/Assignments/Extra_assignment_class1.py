# 1. Write a program which prints 'Hello' on screen and then print your name on
# a separate line.
print("Hello\nMy name is Oshri Shaul")

# 2. Write a program to print the sum of two numbers
num1=2
num2=3
print(num1+num2)

# 3. Write a program which will print the Python version number installed on
# your machine.
import sys
print("My Python version is -->", sys.version)

# 4. Write a program which will reverse a word (e.g. hello  olleh)
string = "abcdefg" [::-1]
print(string)

# 5. Write a program which will print the amount of letters in a given word (e.g.
# hello  5)
word='Home'
print(word, "->", len(word))

# 6. # Write a program which will print the current date and time
import datetime
now = datetime.datetime.now()
print ("The current date and time is:",str(now))

# 7. Write a program which:
# A. contains 2 variables X & Y
# B. Give X & Y values (e.g. X = 1, Y = 5)
x=1
y=5

# C. Using if-else check which is bigger, and print the bigger number.
if x == y:
    print("equals")
elif x > y:
    print(x)
else: print (y)

# 8. Write a program which will check whether or not the number 120 is bigger
# than 5 and smaller than 200, if so, print MATCH
x=120
if x > 5 and x < 200:
    print("MATCH")