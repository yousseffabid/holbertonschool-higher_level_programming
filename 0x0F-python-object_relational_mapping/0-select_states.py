#!/usr/bin/python3
from sys import argv
import MySQLdb
"""List all states"""


if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], host='localhost',
                         port=3306, db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    for row in cur.fetchall():
        print(row)
