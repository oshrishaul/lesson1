import pymysql
# Establishing a connection to DB
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', db='players')
conn.autocommit(True)

# Getting a cursor from Database
cursor = conn.cursor()

# Deleting data into table
cursor.execute("DELETE FROM players.users WHERE name = 'oshri'")

cursor.close()