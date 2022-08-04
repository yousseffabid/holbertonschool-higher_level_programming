#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    args = sys.argv[4].split(';')
    state_name = args[0].strip('"\'')

    cur = db.cursor()
    cur.execute("SELECT * \
                 FROM states \
                WHERE BINARY name = '{}'".format(state_name))
    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
