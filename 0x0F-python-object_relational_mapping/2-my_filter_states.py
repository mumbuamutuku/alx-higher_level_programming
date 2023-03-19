#!/usr/bin/python3
# Lists all states from the database hbtn_0e_0_usa.
# Usage: ./2-my_filter_states.py <mysql username> \
#                             <mysql password> \
#                             <database name>
from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    c = db.cursor()
    sel_cmd = "SELECT * FROM states WHERE name = '{:s}'\
    ORDER BY id ASC".format(argv[4])
    c.execute(sel_cmd)
    u = c.fetchall()
    for state in u:
        if state[1] == argv[4]:
            print(state)
    c.close()
    db.close()

