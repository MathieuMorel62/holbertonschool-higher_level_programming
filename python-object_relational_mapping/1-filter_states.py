#!/usr/bin/python3
"""Lists all states with a name starting with from the database"""


import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    connection = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        password=password,
        database=database
        )

    cursor = connection.cursor()
    cursor.execute("SELECT * from states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")

    results = cursor.fetchall()
    for row in results:
        print(row)

    cursor.close()
    connection.close()
