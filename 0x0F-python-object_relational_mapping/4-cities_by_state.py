#!/usr/bin/python3
"""
Module: defines a script that lists all states with names
like the given argument safely
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    database = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cursor = database.cursor()
    sql = "SELECT cities.id, cities.name, states.name \
            FROM `cities` INNER JOIN `states` \
            ON cities.state_id = states.id \
            ORDER BY cities.id"
    cursor.execute(sql)
    for row in cursor.fetchall():
            print(row)
