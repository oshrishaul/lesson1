# Errors - there are 2 kind of errors in Python:
# 1. Syntax Error
# 2. Exceptions

# Exceptions Handling
# Solution => TRY - EXCEPT mechanism

# Example
# try:
#     x = open("/users/no_folder", 'r')
# except FileNotFoundError:
#     print("file not found!!!")
# print(1234)

# try:
#     x = open("/users/no_folder", 'r')
# except FileNotFoundError as e:
#     print(e) # use that method to print the system error itself
#     print(e, "file not found!!!") # we can add a text off are own
# print(1234)

# Finally - Will appear after TRY. ללא תלות ב Exeption.
# מיועד לאינדיקציה לסימון סיום ריצה / כישלון ריצה של בלוקים של קוד

try:
     # x = open("/users/no_folder", 'r')
    y = open("C:\\Users\\shaulo2\\Desktop\\Python Stuff\\1.txt", 'r')
except FileNotFoundError as e:
    print(e)
finally:
    print("End block A")

# Debugger
# 1. mark break point
# 2. Use "Evaluate Expression" to run debug with one - time value

# Conventions: כללים מוסכמים לגבי כתיבת קוד (קונבנציה)

# PIP - "Pip install packages" or "Pip installs Python" | https://pypi.org
# כלי להתקנת חבילות ומודולים חיצוניים ולא דיפולטייביים
# לאחר ההתקנה, המודול / חבילה יהיו זמינים עבור האינטרפרטר ב Import
