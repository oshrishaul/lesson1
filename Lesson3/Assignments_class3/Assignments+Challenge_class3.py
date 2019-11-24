# 1. Write the following code: a = 1/0;
# 2. Build a corresponding try-except block to avoid exception.
try:
    a = 1/0
except:
    print("It is impossible to divide by zero!")

# 3. Is the following code legal?
# try :
#     x = 1
# finally :
#     print("finally")
# ANSWER - Yes. We can use Try + Finally without dependence in Except. for example - we can use try + finally to get an indication for the end of the block running.

# 4. What exception types can be caught by the following handler?
# Except:
# ANSWER - Except will handle ALL the Exceptions types, since that we didn't use any Exception statement.

#5. What is wrong with using the above type of exception handler? ("Except:")
# ANSWER - Since we didn't use Except with any Except statement (for example - "FileNotFoundError") we can not get the accurate error results of our code.

# 6. What exceptions can be caught by the following handlers?
# except IOError - Handles Input/Output errors
# except ZeroDivisionError - Handles dividing by zero kind of error (impossible mathematical operation).

# 7. Create a text file named “words.txt” programmatically
# 8. Write your name into the file
# 9. Read your file content and print it
# 10. Write Hebrew content into your text file and print its content programmatically.
newfile = open("C:\\Users\\shaulo2\\Desktop\\Python Stuff\\words.txt", 'w+', encoding='utf-8')
newfile.write("My name is Oshri Shaul" + "\n")
newfile.write("שמי הוא אושרי שאול")
newfile.seek(0)
content = newfile.read()
print(content)
newfile.close()
# Challenge:
# 11. Create an image from code (png file) Hint:use Pillow
# In my case, I will create a black rectangle with the written "Great success !!!" on it.
# from PIL import Image, ImageDraw
# Myimage = Image.new('RGB', (220,60), color='black')
# t = ImageDraw.Draw(Myimage)
# t.text((10,10), "Great success !!!")
# Myimage.save("Image.png")

