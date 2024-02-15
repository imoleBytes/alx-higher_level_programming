#!/usr/bin/python3
"""
A script that lists all states with a name starting
with N (upper N) from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    my_user = sys.argv[1]
    my_password = sys.argv[2]
    my_database = sys.argv[3]

    conn = MySQLdb.connect(host="localhost", user=my_user, passwd=my_password, db=my_database, port=3306)
    cur = conn.cursor()

    cur.execute("""SELECT * FROM states WHERE name LIKE BINARY
                'N%' ORDER BY states.id""")
    results = cur.fetchall()

    for rec in results:
        print(rec)
    cur.close()
    conn.close()
