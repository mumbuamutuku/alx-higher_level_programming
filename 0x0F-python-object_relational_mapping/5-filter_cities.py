#!/usr/bin/python3
'''
    Displays all cities of a given state from the
    states table of the database hbtn_0e_4_usa.
    Safe from SQL injections.
    Usage: ./5-filter_cities.py <mysql username> \
                                 <mysql password> \
                                <database name> \
                             <state name searched>
'''
from sys import argv
import MySQLdb

if __name__ == '__main__':
    the_usa = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    commands = the_usa.cursor()
    commands.execute("SELECT cities.id, cities.name, states.name FROM\
    cities JOIN states ON cities.state_id = states.id\
    ORDER BY cities.id ASC")
    us = commands.fetchall()
    coma = 0
    for state in us:
        if state[2] == argv[4]:
            if coma > 0:
                print(", ", end="")
            print("{:s}".format(state[1]), end="")
            coma += 1
    print("")
    commands.close()
    the_usa.close()
