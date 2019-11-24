import pymysql
# Establishing a connection to DB
# conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', db='players')
conn = pymysql.connect(host='remotemysql.com', port=3306, user='FqonWkfpH9', passwd='SuamaJxhsQ', db='FqonWkfpH9')
conn.close()
# # Getting a cursor from Database
# cursor = conn.cursor()
#
# # Getting all data from table “users”
# cursor.execute("SELECT * FROM players.users;") # use scheme.table
#
# # Iterating table and printing all users
# for row in cursor:
#     print(row)
#
# cursor.close()
# conn.close()

# go to ==> https://github.com/Dgotlieb/Python-MySQL