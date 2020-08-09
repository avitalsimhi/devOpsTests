# Establishing a connection to DB
import pymysql

conn = pymysql.connect(host='remotemysql.com', port=3306, user='deWURQVmA4', passwd='4BiPfX3o8l', db='deWURQVmA4')

# Getting a cursor from Database
cursor = conn.cursor()

# Getting all data from table “users”
cursor.execute("SELECT * FROM deWURQVmA4.users;")

# Iterating table and printing all users
for row in cursor:
    print(row)

cursor.close()
conn.close()
