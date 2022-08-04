#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    args = sys.argv[4].split(';')
    state_name = args[0].strip('"\'')

    cur = db.cursor()
    cur.execute("SELECT cities.name \
                 FROM cities \
                INNER JOIN states \
                ON cities.state_id = states.id \
                WHERE BINARY states.name = '{}' \
                ORDER BY cities.id".format(state_name))

    print(", ".join([row[0] for row in cur.fetchall()]))

    cur.close()
    db.close()
