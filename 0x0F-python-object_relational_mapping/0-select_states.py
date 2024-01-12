#!/usr/bin/python3
import MySQLdb
import sys

"""This module contains the mail function which connect to the database"""


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
    cur.execute("SELECT * FROM states")
    results = cur.fetchall()

    printall(results)


if __name__ == "__main__":
    main()
