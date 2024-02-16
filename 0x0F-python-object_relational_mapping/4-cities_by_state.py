#!/usr/bin/python3
"""
Write a script that lists all cities from the database
hbtn_0e_4_usa.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    my_user = sys.argv[1]
    my_password = sys.argv[2]
    my_database = sys.argv[3]

    conn = MySQLdb.connect(host="localhost", user=my_user, passwd=my_password,
                           db=my_database, port=3306)
    cur = conn.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name FROM cities
                JOIN states ON states.id = cities.states_id
                ORDER BY cities.id ASC""")
    results = cur.fetchall()

    for rec in results:
        print(rec)
    cur.close()
    conn.close()
