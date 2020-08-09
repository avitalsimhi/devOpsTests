# Establishing a connection to DB
import pymysql

# conn = pymysql.connect(host='remotemysql.com', port=3306, user='GABDn8UF3c', passwd='f89980EmXo', db='GABDn8UF3c')
conn = pymysql.connect(host='remotemysql.com', port=3306, user='GABDn8UF3c', passwd='NCPHIbMHg6', db='GABDn8UF3c')
conn.autocommit(True)

# Getting a cursor from Database
cursor = conn.cursor()

# Inserting data into table
cursor.execute("INSERT into GABDn8UF3c.users (id, name) VALUES (3, 'Sara')")

cursor.close()
conn.close()