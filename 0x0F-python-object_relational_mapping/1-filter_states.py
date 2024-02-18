#!/usr/bin/python3
"""
Module: defines a script that lists all states with names starting with 'N'
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    database = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cursor = database.cursor()
    cursor.execute("SELECT * FROM `states` ORDER BY id")
    for row in cursor.fetchall():
        if row[1][0] == 'N':
            print(row)
