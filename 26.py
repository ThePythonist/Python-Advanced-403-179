import sqlite3

conn = sqlite3.connect("info.db")
cur = conn.cursor()

people = [
    {"name": "farzad", "field": "computer", "grade": 17.65},
    {"name": "kiana", "field": "bargh", "grade": 14.30},
    {"name": "alireza", "field": "memari", "grade": 18.25},
    {"name": "maryam", "field": "shimi", "grade": 16.90},
]


def create():
    command = "CREATE TABLE IF NOT EXISTS students (name,field,grade);"
    cur.execute(command)
    conn.commit()
    print("Table Students Created")


def insert(person):
    command = f"INSERT INTO students VALUES {(person['name'], person['field'], person['grade'])};"
    cur.execute(command)
    conn.commit()
    print("Successfuly Inserted")


def select():
    command = "SELECT * FROM students;"
    cur.execute(command)
    students = cur.fetchall()
    for i in students:
        print(i)


# create()

# for i in people:
#     insert(i)

select()
