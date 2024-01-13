#!/usr/bin/python3
"""module contains main function which connect to a database"""
import MySQLdb
import sys


def main():
    """conect to database"""
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    conn = MySQLdb.connect(host="localhost", user=user, passwd=password,
                           db=database, port=3306)
    cur = conn.cursor()
    command = """SELECT cities.id, cities.name, states.name FROM cities INNER
            JOIN states ON states.id=cities.state_id ORDER BY cities.id ASC"""
    cur.execute(command)
    results = cur.fetchall()

    for row in results:
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
