#!/usr/bin/python3
"""
    This script takes in the name of a state as an argument and lists all
    cities of that state from the hbtn_0e_4_usa database, sorted in
    ascending order by cities.id.
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
        "SELECT cities.name\
        FROM cities\
        JOIN states ON cities.state_id = states.id\
        WHERE states.name=%s\
        ORDER BY cities.id ASC", (state_name,)
        )

    cities = cursor.fetchall()
    if cities:
        print(", ".join(city[0] for city in cities))
    else:
        print()

    cursor.close()
    connection.close()
