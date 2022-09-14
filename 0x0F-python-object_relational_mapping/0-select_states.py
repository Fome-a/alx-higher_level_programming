#!/usr/bin/python3
"""
python script that lists all states from the database hbtn_0e_0_usa
"""
import sys

if __name__ == "__main__":
    import MYSQLdb
    if (len(sys.argv)== 4):
        user=sys.argv[1]
        password=sys.argv[2]
        database=sys.argv[3]
    db = MYSQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=password,
        db=database)
    cur=db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows= cur.fetchall()
    for row in rows:
        print(rows)
    cur.close() #close all cursors
    db.close()#close all rows