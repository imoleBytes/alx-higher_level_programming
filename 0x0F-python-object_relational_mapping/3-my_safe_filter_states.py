#!/usr/bin/python3

"""This module contains the main function which connect to the database"""

import MySQLdb
import sys


# def main():
#     """Progrms statrts here!"""
#     conn = MySQLdb.connect(host="localhost", user=sys.argv[1],
#  passwd=sys.argv[2], db=)

# stmnt = """SELECT * FROM states WHERE name LIKE BINARY '{}'
# ORDER BY states.id ASC"""

def connect(host, user, passwd, database, port):
    """connect to db"""
    conn = MySQLdb.connect(host=host, user=user, passwd=passwd,
                           db=database, port=port)
    return conn


def getCursor(c):
    """gets cursor to work on"""
    return c.cursor()


def execute(cur, statement):
    """executes statements"""
    results = cur.execute(statement, (sys.argv[4], )).fetchall()
    return results


def printall(rows):
    """prints all results"""
    for row in rows:
        print(row)


def main():
    """main program starts here"""
    db = connect("localhost", sys.argv[1], sys.argv[2], sys.argv[3], 3306)

    cur = getCursor(db)
    command = """SELECT * FROM states WHERE name LIKE %s
                    ORDER BY states.id ASC"""
    rows = execute(cur, command)
    printall(rows)
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
