#!/usr/bin/python3
""" This module takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE BINARY name='{}' ORDER BY id"
                .format(sys.argv[4]))
    query_rows = cur.fetchall()
    for state in query_rows:
        print(state)
    cur.close()
    conn.close()
