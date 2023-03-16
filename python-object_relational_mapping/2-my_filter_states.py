#!/usr/bin/python3
"""
Displays all values in the states table of hbtn_0e_0_usa
where name matches the argument
"""


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
    cursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY '{}'".format(sys.argv[4])
        )

    results = cursor.fetchall()
    for row in results:
        print(row)

    cursor.close()
    connection.close()
