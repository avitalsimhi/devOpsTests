import pymysql

conn = pymysql.connect(host='remotemysql.com', port=3306, user='GABDn8UF3c', passwd='NCPHIbMHg6', db='GABDn8UF3c')

# Getting a cursor from Database
conn.autocommit(True)
cursor = conn.cursor()


#2
cursor.execute("INSERT into GABDn8UF3c.dogs (name, age, breed) VALUES ('joni', 10, 'asia')")
cursor.execute("INSERT into GABDn8UF3c.dogs (name, age, breed) VALUES ('lex', 3, 'blabla')")
cursor.execute("INSERT into GABDn8UF3c.dogs (name, age, breed) VALUES ('yan', 8, 'ggg')")

#3
cursor.execute("UPDATE GABDn8UF3c.dogs set breed = 'asia' where name = 'lex'")

#4
cursor.execute("DELETE FROM GABDn8UF3c.dogs where name = 'yan'")

# Getting all data from table “dogs”
cursor.execute("SELECT * FROM GABDn8UF3c.dogs;")

# Iterating table and printing all users
for row in cursor:
    print(row)

cursor.close()
conn.close()
