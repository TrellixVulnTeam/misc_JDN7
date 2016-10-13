import sqlite3
import os
import re


def get_sqlite_conn(sqlite_file):
    """get sqlite connection giving path of database file.
    args:
        sqlite_file (str): path of sqlite database file.
    return:
        connection object
    """
    if os.path.isfile(sqlite_file):
        print("DB already exists: " + sqlite_file)
        conn = sqlite3.connect(sqlite_file)
        # conn = sqlite3.connect(":memory:")
        # load local sqlite file entirely into memory:
        # http://stackoverflow.com/questions/3850022/how-to-load-existing-db-file-to-memory-in-python-sqlite3
    else:
        print("creating new database file: " + sqlite_file)
        conn = sqlite3.connect(sqlite_file)
        # Create table
        conn.execute('CREATE TABLE stocks (date text, trans text, symbol text,'
                     'qty real, price real)')
        print("created table")

        # Larger example that inserts many records at a time
        purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
                     ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
                     ('2006-04-06', 'SELL', 'IBM', 500, 53.00), ]
        conn.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)
        print("inset data")

        # Save (commit) the changes
        conn.commit()

    # add REGEXP support
    def regexp(expr, item):
        reg = re.compile(expr)
        return reg.search(item) is not None

    conn.create_function("REGEXP", 2, regexp)

    return conn


sqlite_file = 'example.sqlite'
conn = get_sqlite_conn(sqlite_file)

# do something here !
t = ('IBM', )
result = conn.execute('SELECT * FROM stocks WHERE symbol=?', t)
print(result.fetchone())
r = conn.execute("SELECT * FROM stocks")
print(r.fetchone())

print("regex")
# comma is necessary for tuple
regex = ("I.*", )
# emit comma in list
regex = ["I.*"]
result = conn.execute('SELECT * FROM stocks WHERE symbol REGEXP ?', regex)
print(result.fetchone())
print(result.fetchone())

conn.close()
