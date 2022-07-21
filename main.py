# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import psycopg2

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi 1, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def print_hi2():
    # Use a breakpoint in the code line below to debug your script.
    print(f' in db connect part ')  # Press Ctrl+F8 to toggle the breakpoint.
    # Connect to your postgres DB
    # conn = psycopg2.connect("dbname=test user=postgres")
    conn = psycopg2.connect("host=ubu dbname=test user=postgres password=BunnyDB1")
    print(f'in create table part ')  # Press Ctrl+F8 to toggle the breakpoint.
    cur = conn.cursor()
    cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")
    cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)",(100, "abc'def"))
    cur.execute("SELECT datname from pg_database")
    rows = cur.fetchall()
    print ( "\nShow me the databases:\n")
    for row in rows:
        print("   ", row[0])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print_hi2()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
