#!/usr/bin/python3
"""
Lists all states with a name starting with N (upper N) from hbtn_0e_0_usa.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    name_arg = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name,
        charset="utf8"
    )

    cursor = db.cursor()
    cur_query = "SELET * FROM states WHERE name = '{}' ORDER BY id ASC".format(
        name_arg)
    cursor.execute(cur_query)
    query = cursor.fetchall()

    for row in query:
        print(row)

    cursor.close()
    db.close()
