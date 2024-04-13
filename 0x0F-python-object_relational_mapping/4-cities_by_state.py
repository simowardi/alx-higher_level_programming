#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys


if __name__ == "__main__":
    # Establishing a connection to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )
    # Creating a cursor object to execute SQL queries
    cur = db.cursor()

    # Executing the SQL query to select cities with their respective states
    cur.execute("""SELECT cities.id, cities.name, states.name FROM
                cities INNER JOIN states ON states.id=cities.state_id""")

    # Fetching all the rows resulted from the query
    rows = cur.fetchall()

    # Printing each row
    for row in rows:
        print(row)

    # Closing the cursor and database connection
    cur.close()
    db.close()
