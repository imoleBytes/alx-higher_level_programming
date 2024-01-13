#!/usr/bin/python3
"""This module contains the main function which connect to the database"""
import MySQLdb
import sys


if __name__ == "__main__":
    # main()
    conn = MySQLdb.connect(host="localhost", user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = conn.cursor()
    cur.execute("""SELCECT * FROM states WHERE name LIKE BINARY'%s'
                ORDER BY states.id ASC""", (sys.argv[4], ))
    results = cur.fetchall()
    for row in results:
        print(row)
    cur.close()
    conn.close()
