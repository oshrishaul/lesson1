import pymysql
# Establishing a connection to DB
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', db='players')
conn.autocommit(True)

# Getting a cursor from Database
cursor = conn.cursor()

# Updating data inside the table
cursor.execute("UPDATE players.users SET id = '10' WHERE name = 'oshri'")

cursor.close()
conn.close()