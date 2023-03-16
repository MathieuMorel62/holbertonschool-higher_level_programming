#!/usr/bin/python3
"""
    This script takes in arguments and displays all values in the states table
    of hbtn_0e_0_usa where name matches the argument.
    But this time, it is safe from MySQL injections!
"""


import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    connection = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        password=password,
        database=database
        )

    cursor = connection.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE BINARY name = %s ORDER BY id",
        (state_name,)
        )

    results = cursor.fetchall()
    for row in results:
        print(row)

    cursor.close()
    connection.close()
