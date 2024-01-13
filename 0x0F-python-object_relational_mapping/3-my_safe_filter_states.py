#!/usr/bin/python3

"""This module contains the main function which connect to the database"""

def main():
    """Progrms statrts here!"""
    conn = MySQLdb.connect(host="localhost", user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("""SELCECT * FROM states WHERE name LIKE BINARY'%s'
                ORDER BY states.id ASC""", (sys.argv[4], ))
    results = cur.fetchall()
    printall(results)
    cur.close()
    conn.close()


def printall(rows):
    """prints all results"""
    for row in rows:
        print(row)


if __name__ == "__main__":
    import MySQLdb
    import sys
    main()
