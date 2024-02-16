#!/usr/bin/python3
"""
a script that takes in arguments and displays all values in
the states table of hbtn_0e_0_usa where name matches the
argument. But this time, write one that is safe from MySQL
injections!.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    my_user = sys.argv[1]
    my_password = sys.argv[2]
    my_database = sys.argv[3]
    state_name = sys.argv[4]

    conn = MySQLdb.connect(host="localhost", user=my_user, passwd=my_password,
                           db=my_database, port=3306)
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE %s", (state_name, ))
    results = cur.fetchall()

    for rec in results:
        print(rec)
    cur.close()
    conn.close()
