import sqlite3

conn = sqlite3.connect("example.db")  # etesal ya sakht database
cur = conn.cursor()  # cursor baraye ejraye dastoorat sql

# CRUD : Create, Read, Update, Delete

# cur.execute("CREATE TABLE students (name,age,degree);")

# cur.execute("INSERT INTO students VALUES ('mobina',21,'bachelor');")
# cur.execute("INSERT INTO students VALUES ('behrad',17,'diploma');")
# cur.execute("INSERT INTO students VALUES ('amirali',16,'diploma');")

cur.execute("SELECT * FROM students;")
students = cur.fetchall()
print(students)

# for i in students:
#     print(i)

conn.commit()
conn.close()
