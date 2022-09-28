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
        name_search= sys.argv[4]
        conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=user,
            passwd=password,
            db=database,
            charset="utf8")
        cur = conn.cursor()
        id=input("Enter State name: ")
        my_data=(id,)
        cur.execute("SELEct * FROM states WHERE name LIKE '%s'".format(sys.argv[4]))
        query_rows=cur.fetchall()
        for row in query_rows:
            print(row) 
        cur.close()
        conn.close()