import sqlite3


def create():
    con = sqlite3.connect("info.db")
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS employees(
    id INTEGER PRIMARY KEY,
    name VARCHAR(50),
    code INTEGER,
    job VARCHAR(70)
    );
    """)
    con.commit()
    con.close()


def select():
    con = sqlite3.connect("info.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM employees;")
    records = cur.fetchall()
    for i in records:
        print(i)


def insert(record):
    con = sqlite3.connect("info.db")
    cur = con.cursor()

    query = f"SELECT * FROM employees;"
    cur.execute(query)
    records = cur.fetchall()

    for i in records:
        if i[1] == record['name'] and i[2] == record['code'] and i[3] == record["job"]:
            print("Data already exists")
            break
    else:
        query = f"""
        INSERT INTO employees (name,code,job)
        VALUES {(record['name'], record['code'], record['job'])};"""
        cur.execute(query)

        con.commit()
        con.close()


create()
insert({"name": "Mohammad", "code": 40215, "job": "Civil Engineer"})
select()
