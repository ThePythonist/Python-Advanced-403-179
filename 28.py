import sqlite3


def create_table():
    conn = sqlite3.connect("User-Database.db")
    cur = conn.cursor()

    table_name = input('Enter table name : ')
    columns = input(f"Enter table {table_name} columns (separated by comma) : ").split(",")

    query = f"CREATE TABLE IF NOT EXISTS {table_name} {tuple(columns)};"
    cur.execute(query)
    print(f"Created table {table_name}")

    conn.commit()
    conn.close()


def insert():
    # Later
    pass


def select():
    con = sqlite3.connect("User-Database.db")
    cur = con.cursor()

    table_name = input('Enter table name : ')

    query = f"SELECT * FROM {table_name};"

    try:
        cur.execute(query)
        records = cur.fetchall()

        for i in records:
            print(i)
    except sqlite3.OperationalError:
        print("Table doesnt exists")


def main():
    choice = input("""
Hello Welcome To Database Manager
Choose an operation
1 : Create a table
2 : Insert a record into table
3 : Show table records
4 : Exit 
Choice : """)

    if choice == "1":
        create_table()
    elif choice == "2":
        insert()
    elif choice == "3":
        select()
    elif choice == "4":
        # return None
        exit()
    else:
        print("Invalid operation. Try again")
        main()


while True:
    main()
