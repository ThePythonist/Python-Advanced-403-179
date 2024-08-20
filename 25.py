import sqlite3

conn = sqlite3.connect("info.db")
cur = conn.cursor()

# cur.execute("INSERT INTO customers VALUES ('shayan','yazd','09936226030');")
# cur.execute("INSERT INTO customers VALUES ('samyar','ramsar','09110919030');")
# cur.execute("INSERT INTO customers VALUES ('niloofar','andimeshk','09163225010');")

# cur.execute("DELETE FROM customers;")  # Deletes every record in table

cur.execute("SELECT * FROM customers;")
customers = cur.fetchall()

for i in customers:
    print(i[2])


# cur.execute("SELECT phone FROM customers;")
# customers = cur.fetchall()
#
# for i in customers:
#     print(i[0])

conn.commit()
conn.close()
