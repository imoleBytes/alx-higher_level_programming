#!/usr/bin/python3

import MySQLdb
import sys


# stmnt = """SELECT * FROM states WHERE name LIKE BINARY '{}'
# ORDER BY states.id ASC"""


def connect(host, user, passwd, database, port):
    conn = MySQLdb.connect(host, user, passwd, database, port)
    return conn


def getCursor(c):
    return c.cursor()


def execute(cur, statement):
    results = cur.execute(statement)
    return results


def printall(rows):
    for row in rows:
        print(row)


def main():
    db = connect("localhost", sys.argv[1], sys.argv[2], sys.argv[3], 3306)

    cur = getCursor(db)

    rows = execute(cur, """SELECT * FROM states WHERE name LIKE BINARY '{}'
                   ORDER BY states.id ASC""")
    printall(rows)


if __name__ == "__main__":
    main()
