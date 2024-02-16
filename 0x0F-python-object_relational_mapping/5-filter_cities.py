#!/usr/bin/python3
"""
Write a script that takes in the name of a state as an
argument and lists all cities of that state, using the
database hbtn_0e_4_usa.
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
    cur.execute("""SELECT cities.name FROM cities INNER JOIN
                states ON states.id = cities.state_id WHERE
                states.name = %s""", (state_name, ))
    results = cur.fetchall()

    tmp = list(row[0] for row in results)
    print(*tmp, sep=", ")
    cur.close()
    conn.close()
