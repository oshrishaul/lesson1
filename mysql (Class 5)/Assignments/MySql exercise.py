import pymysql
conn = pymysql.connect(host='remotemysql.com', port=3306, user='FqonWkfpH9', passwd='SuamaJxhsQ', db='FqonWkfpH9')
conn.autocommit(True)
cursor = conn.cursor()
#2. Insert 3 dogs with different values
cursor.execute("INSERT into FqonWkfpH9.dogs (name, age, breed) VALUES ('baki', 3, 'amstaf')")
cursor.execute("INSERT into FqonWkfpH9.dogs (name, age, breed) VALUES ('nets', 1, 'lavrador')")
cursor.execute("INSERT into FqonWkfpH9.dogs (name, age, breed) VALUES ('mika', 2, 'pomeranian')")

#3. Update second dog age from one value to another
cursor.execute("UPDATE FqonWkfpH9.dogs SET age = '5' WHERE name = 'nets'")

#4. Delete the third dog from table
cursor.execute("DELETE FROM FqonWkfpH9.dogs WHERE name = 'mika'")

#5. Query table and print all dogs names.
cursor.execute("SELECT * FROM FqonWkfpH9.dogs;")
for row in cursor:
    print(row)
cursor.close()
conn.close()
