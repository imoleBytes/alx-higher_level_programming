#!/usr/bin/python3
"""A scripts that lists all states from a database 'hbtn_0e_0_usa'"""
import MySQLdb
import sys


if __name__ == "__main__":
    args = sys.argv
    my_host = "localhost"
    my_user = args[1]
    my_password = args[2]
    my_database = args[3]
    port = 3306

    conn = MySQLdb.connect(host=my_host, user=my_user,
                           passwd=my_password, db=my_database, port=port)

    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id")
    results = cur.fetchall()

    for record in results:
        print(record)

    cur.close()
    conn.close()
