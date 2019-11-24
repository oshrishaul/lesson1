 # How to open a file and getting a content
# My_file = open("C:\\Users\\shaulo2\\Desktop\\Python Stuff\\1.txt", 'w+')
# My_file.write("text added successfully")
# My_file.seek(0) #Will take the CURSOR to the begining of the file for reading
# content = My_file.read() # now it will read from the very first begining
# print(content)
# My_file.close() # will ensure that the access to the file will end for sure

#My_file2 = open("C:\\Users\\shaulo2\\Desktop\\Python Stuff\\2.txt", 'w+') # Will create a new file in case of missing file

My_file = open("C:\\Users\\shaulo2\\Desktop\\Python Stuff\\1.txt", "r")
content = My_file.read()
print(content)

