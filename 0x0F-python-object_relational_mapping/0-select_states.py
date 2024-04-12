#!/usr/bin/python3
"""
A script to retrieve and display all states from a MySQL database.

Usage:
    ./0-select_states.py <username> <password> <database>
"""

import sys
import MySQLdb


def select_states(username, password, database):
    """
    Connects to the MySQL database and retrieves all states,
    displaying them in ascending order by state ID.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Name of the MySQL database.

    Returns: None
    """
    # Connect to the database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8"
    )

    # Create a cursor object
    cur = db.cursor()

    # Execute the query
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all rows
    rows = cur.fetchall()

    # Display the results
    for row in rows:
        print(row)

    # Close the cursor and connection
    cur.close()
    db.close()


if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Get command line arguments
    username, password, database = sys.argv[1:4]
    # Call the select_states function with the provided arguments
    select_states(username, password, database)
