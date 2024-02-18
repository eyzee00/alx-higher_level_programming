#!/usr/bin/python3
"""
Module: defines a script that lists all states with names
like the given argument
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    database = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cursor = database.cursor()
    sql = "SELECT * FROM `states` WHERE BINARY name='{}'".format(argv[4])
    cursor.execute(sql)
    for row in cursor.fetchall():
        print(row)
