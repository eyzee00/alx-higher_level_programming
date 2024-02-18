#!/usr/bin/python3
"""
Module: define a script that lists all states
from hbtn_0e_0_usa
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    database = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cursor = database.cursor()
    cursor.execute("SELECT * FROM `states` ORDER BY `states.id` ASC")
    for row in cursor.fetchall():
        print(row)
