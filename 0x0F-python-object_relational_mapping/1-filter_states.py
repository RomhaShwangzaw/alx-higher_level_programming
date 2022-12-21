#!/usr/bin/python3
""" This module lists all states, that start with 'N',
from the database hbtn_0e_0_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    query_rows = cur.fetchall()
    for id, name in query_rows:
        print("({}, '{}')".format(id, name))
    cur.close()
    conn.close()
