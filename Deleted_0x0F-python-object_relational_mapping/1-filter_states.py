#!/usr/bin/python3
"""This module contains the main function which connect to the database"""


def printall(rows):
    """prints all rows in results"""
    for row in rows:
        print(row)


def main():
    """Function connect to the database at localhost"""
    conn = MySQLdb.connect(host="localhost", user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3],
                           port=3306)
    cur = conn.cursor()
    cur.execute("""SELECT * FROM states
                WHERE name LIKE BINARY 'N%'
                ORDER BY states.id ASC"""
                )
    results = cur.fetchall()

    printall(results)
    cur.close()
    conn.close()


if __name__ == "__main__":
    import MySQLdb
    import sys

    main()
