import sqlite3

conn = sqlite3.connect("info.db")
cur = conn.cursor()

cur.execute("CREATE TABLE customers (name,city,phone);")

conn.commit()
conn.close()
