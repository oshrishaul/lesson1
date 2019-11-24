import pymysql
# Establishing a connection to DB
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', db='players')
conn.autocommit(True)

# Getting a cursor from Database
cursor = conn.cursor()

# Inserting data into table
cursor.execute("INSERT into players.users (name, id) VALUES ('oshri', 2)")
cursor.execute("INSERT into players.users (id, name) VALUES (1, 'john')")
cursor.close()
conn.close()