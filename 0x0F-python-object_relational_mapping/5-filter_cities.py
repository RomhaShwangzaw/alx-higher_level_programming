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
    searched = sys.argv[4]
    cur.execute("""SELECT c.name \
                FROM cities c \
                JOIN states s \
                ON c.state_id = s.id \
                WHERE BINARY s.name = %(searched_state)s
                ORDER BY c.id""",
                {'searched_state': searched})
    query_rows = cur.fetchall()
    cities = []
    for city in query_rows:
        cities.append(city[0])
    print(", ".join(cities))
    cur.close()
    conn.close()
