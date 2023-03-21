#!/usr/bin/python3
'''
    Lists all cities of the database hbtn_0e_4_usa, ordered by city id.
    Usage: ./4-cities_by_state.py <mysql username> \
                               <mysql password> \
                               <database name>
'''
from sys import argv
import MySQLdb

if __name__ == '__main__':
    the_usa = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    commands = the_usa.cursor()
    commands.execute("SELECT cities.id, cities.name, states.name FROM\
    cities JOIN states ON cities.state_id = states.id")
    us = commands.fetchall()
    for state in us:
        print(state)
    commands.close()
    the_usa.close()
