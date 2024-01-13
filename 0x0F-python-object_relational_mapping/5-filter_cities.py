#!/usr/bin/python3
"""module contatins main function working on the datatbase"""
import MySQLdb
import sys


def main():
    """connects to datatbase"""
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    conn = MySQLdb.connect(host="localhost", user=username, passwd=password,
                           db=database, port=3306)
    cur = conn.cursor()
    command = """SELECT cities.name FROM cities INNER JOIN states ON
                state.id=cities.state_id WHERE state.name LIKE BINARY
                %s ORDER BY cities.id ASC"""
    cur.execute(command, (state_name, ))
    result = cur.fetchall()

    for row in result[:-1]:
        print(row[0], sep=", ")
    print(result[-1][0])

    cur.close()
    conn.close()
