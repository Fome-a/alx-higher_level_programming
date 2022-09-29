#!/usr/bin/python3
"""
python script that lists out the states name corresponding with user input from the database hbtn_0e_0_usa preventing injection
"""

import sys

if __name__ == "__main__":
    import MySQLdb
    if (len(sys.argv) == 5):
        user = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=user,
            passwd=password,
            db=database,
            charset="utf8")
        cur = conn.cursor()
        cur.execute("SELECT states.name, cities.name FROM states, cities WHERE ID = state_id ORDER BY state_id ASC")
        query_rows=cur.fetchall()
        for row in query_rows:
            print(row) 
        cur.close()
        conn.close()