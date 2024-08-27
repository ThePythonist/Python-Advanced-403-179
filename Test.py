import sqlite3

con = sqlite3.connect("info.db")
cur = con.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS employees(
id INT PRIMARY KEY,
name VARCHAR(50),
code INT,
job VARCHAR(70)
);
""")

# cur.execute("INSERT INTO employees(name,code,job) VALUES ('james',111,'guitar player');")
# cur.execute("INSERT INTO employees(name,code,job) VALUES ('lars',112,'drummer');")
#
# cur.execute("SELECT * FROM employees;")
# records = cur.fetchall()
# for i in records:
#     print(i)

con.commit()
con.close()
