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
    sql = "SELECT cities.name FROM cities \
            INNER JOIN states \
            ON cities.state_id = state.id \
            ORDER BY cities.id"
    cursor.execute(sql)
    string_list = list(cursor.fetchall())
    for index in range(0, len(string_list)):
        if string_list[index] == argv[4]:
            print(string_list[index])
            if index != len(string_list) - 1:
                print(", ", end="")
            else:
                print("")
